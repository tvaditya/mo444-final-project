# -*- coding: utf-8 -*-

import pandas as pd
import statsmodels.api as sm
from constants import *
import data_helper
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import numpy as np
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from classifier import get_voting_classifier

class VotingClassifier:

    def __init__(self, data_path, estimators = 100):
        self.result = 0
	self.train_cols = []
	self.csv = data_helper.read_csv(data_path)
        self.classifier = None
        self.mean_values = {}
        self.std_values = {}
        self.estimators = estimators
        self.train_size = len(self.csv) / 2

    def start_data(self):

        self.train_cols = self.csv.columns.values[1:]

        self.x_train = self.csv[self.train_cols][:self.train_size]
        self.y_train = self.csv[0][:self.train_size]
        self.x_test = self.csv[self.train_cols][self.train_size:]
        self.y_test = self.csv[0][self.train_size:]

        print "Size A: " + str(len(self.x_train))
        print "Size B: " + str(len(self.x_test))


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

    def get_smote_data_frame(self, initial_train_smote):
        train_smote = initial_train_smote

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

        return train_smote

    def get_proportion(self, train_smote):
        groupby = train_smote.groupby([0])
        dict_proportion = {}
        # Prints the proportion of each group (interesse/nao interesse)
        for name, group in groupby:
            entry = len(group)
            proportion = entry / float(len(train_smote))
            print "Group Name: " + str(name) + " / " + str(proportion)
            dict_proportion[name] = proportion
        return dict_proportion

    def train(self):

        print "\nTrain: "

        # Initialize a Voting Classifier
        self.classifier = get_voting_classifier()

        train_smote = pd.DataFrame(self.y_train)
        train_smote = train_smote.join(self.x_train)
        train_smote = self.get_smote_data_frame(train_smote)

        proportion = self.get_proportion(train_smote)
        # If data is not balanced, applies smote again
        if proportion[1] < 0.45:
            train_smote = self.get_smote_data_frame(train_smote)
            self.get_proportion(train_smote)

        # Fit the forest to the training set, using the bag of words as 
        # features and the sentiment labels as the response variable
        #
        # This may take a few minutes to run
        self.classifier = self.classifier.fit( train_smote[self.train_cols], train_smote[0])

###################################################################

    def test(self):
        print "\nTest:"

        # Use the classifier to make predictions
        result = self.classifier.predict(self.x_test)

        # Initializing the Confusion Matrix
        tp = 0
        fn = 0
        fp = 0
        tn = 0

        self.create_confusion_matrix()
	for i in range(0, len(self.y_test)):
	    current_entry = self.y_test.iloc[i]
            if current_entry == result[i]:
                if current_entry == 1:
                    tp += 1
                else:
                    tn += 1
            else:
                if current_entry == 1:
                    fn += 1
                else:
                    fp += 1
            self.confusion_matrix[str(int(current_entry))][str(int(result[i]))] += 1

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
        if tp + fn == 0 or fp + tn == 0:
            print "Either TP + FN or FP + TN is equal to zero"
            return
        normalized_accuracy.append(tp / float(tp+fn))
        normalized_accuracy.append(tn / float(fp+tn))

        print "\nNormalized Accuracy: "
        print normalized_accuracy
        print sum(normalized_accuracy) / 2.0

        print "Accuracy: "
        print (tp + tn) / float(tp + fn + fp + tn)

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

