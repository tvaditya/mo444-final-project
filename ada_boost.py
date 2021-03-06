# -*- coding: utf-8 -*-

import pandas as pd
import statsmodels.api as sm
from constants import *
import data_helper
import random
from sklearn.ensemble import AdaBoostClassifier
import numpy as np
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split

class AdaBoost:

    def __init__(self, data_path, estimators = 100, learning_rate=0.1):
        self.result = 0
	self.train_cols = []
	self.csv = data_helper.read_csv(data_path)
        self.adaboost = None
        self.mean_values = {}
        self.std_values = {}
        self.estimators = estimators
        self.learning_rate = learning_rate
        self.train_size = len(self.csv) / 2

    def start_data(self):

        self.train_cols = self.csv.columns.values[1:]

        self.x_train = self.csv[self.train_cols][:self.train_size]
        self.y_train = self.csv[0][:self.train_size]
        self.x_test = self.csv[self.train_cols][self.train_size + 1:]
        self.y_test = self.csv[0][self.train_size + 1:]

        print "Size A: " + str(len(self.x_train))
        print "Size B: " + str(len(self.x_test))

        print "AdaBoost: \n Estimators = " + str(self.estimators) + "\n Learning Rate = " + str(self.learning_rate)

    def split_data(self):
        print "split_data"

        self.train_cols = self.csv.columns.values[1:]

        x = self.csv[self.train_cols]
        y = self.csv[0]

        # Split the data into a training set and a test set
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, random_state=0, train_size = 0.5)

        print "Size A: " + str(len(self.x_train))
        print "Size B: " + str(len(self.x_test))

    def get_smote_value(self, current_item, previous_item):
        # It starts with 1, which is the value of the class of interest
        new_item = [1]

        for column in self.train_cols:
            new_item.append((current_item[column] + previous_item[column]) / 2.0)

        return new_item

    def train_ada_boost(self):

        print "\nTrain: "

        # Initialize the classifier
        self.adaboost = AdaBoostClassifier(n_estimators = self.estimators, learning_rate=self.learning_rate)

        train_smote = pd.DataFrame(self.y_train)
        train_smote = train_smote.join(self.x_train)

        previous_item = None
        smoted_items = []
        for i in range(0, len(train_smote)):
            entry = train_smote.iloc[i]
            if entry[0] == 1:
                if not(previous_item is None):
                    smoted_item = self.get_smote_value(entry, previous_item)
                    smoted_items.append(smoted_item)
                previous_item = entry

        # Adds the smoted itens in the data frame
        df_smoted_items = pd.DataFrame(smoted_items, columns = self.csv.columns.values)
        train_smote = pd.concat([train_smote, df_smoted_items])

        # Fit the classier to the training set, using the bag of words as 
        # features and the sentiment labels as the response variable
        #
        # This may take a few minutes to run
        self.adaboost = self.adaboost.fit( train_smote[self.train_cols], train_smote[0])

        # Prints the propotion of each group (interesse/nao interesse)
        for name, group in train_smote.groupby([0]):
            entry = len(group)
            print "Group Name: " + str(name) + " / " + str( entry / float(len(train_smote)))

###################################################################

    def test_ada_boost(self):
        print "\nTest:"

        # Use the classifier to make sentiment label predictions
        result = self.adaboost.predict(self.x_test)

        #print result

	right = 0
	wrong = 0

        # Initializing the Confusion Matrix
        tp = 0
        fn = 0
        fp = 0
        tn = 0

        self.create_confusion_matrix()
	for i in range(0, len(self.y_test)):
	    current_entry = self.y_test.iloc[i]
            if current_entry == result[i]:
                right += 1
                if current_entry == 1:
                    tp += 1
                else:
                    tn += 1
            else:
                wrong += 1
                if current_entry == 1:
                    fn += 1
                else:
                    fp += 1
            self.confusion_matrix[str(int(current_entry))][str(int(result[i]))] += 1

	print "Right: " + str(right / float(right + wrong)) 
	print "Wrong: " + str(wrong / float(right + wrong)) + "\n"
        #self.print_confusion_matrix()

        print "      |------------|------------|"
        print "      |   Î        |  NÎ        |"
        print "|-----|------------|------------|"
        print "|  I  | " + str(tp).zfill(5) + " (tp) | " + str(fn).zfill(5) + " (fn) |"
        print "| NI  | "+ str(fp).zfill(5) + " (fp) | " + str(tn).zfill(5) + " (tn) |"
        print "|-----|------------|------------|\n"

        self.print_confusion_matrix(tp, fn, fp, tn)

        # Prints the same confusion matrix using the sklearn implementation
        names = [str(item) for item in range(0,6)]
        print(classification_report(list(self.y_test), list(result), target_names=names))

    def switch_folds(self):
        print "\n2-fold cross validation \nSwitching folds..."

        from copy import copy

        x = self.x_train.copy()
        y = self.y_train.copy()

        self.x_train = self.x_test
        self.y_train = self.y_test

        self.x_test = x
        self.y_test = y


    def print_confusion_matrix(self, tp, fn, fp, tn):
        normalized_accuracy = []
        normalized_accuracy.append(tp / float(tp+fn))
        normalized_accuracy.append(tn / float(fp+tn))

        print "\nNormalized Accuracy: "
        print normalized_accuracy
        print sum(normalized_accuracy) / 2.0

    def print_percent(self, texto):
        lista = texto.strip().split(" ")
        lista = [int(a) for a in lista]
        soma = sum(lista)
        percentuais = [item / float(soma) for item in lista]
        return percentuais

    def format_percent(self, texto, i):
       a = self.print_percent(texto)
       a = [str("{0:.2f}".format(round(item*100,2))) for item in a]
       texto_latex = ""
       for item in a:
           texto_latex += item + " & "
       print str(i) +  " " + texto_latex[:-3]

    def create_confusion_matrix(self):
        confusion_matrix = {}
        for i in range(0, 6):
            label_i = str(i)
            confusion_matrix[label_i] = {}
            for j in range(0, 6):
                confusion_matrix[label_i][str(j)] = 0
        self.confusion_matrix = confusion_matrix

