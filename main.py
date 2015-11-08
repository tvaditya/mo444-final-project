__author__ = 'jose'

import pandas as pd
import print_functions, vectorization, data_helper#, tfidf
from constants import *

train_size = 1000 # 15000

csv = data_helper.read_csv(raw_directory + "out-july-2015-dou.out")

#print "Train size: " + str(train_size)

# Slice the data to get the training data
train = csv[:][:train_size]

clean_description_list = data_helper.clean_list(train)
for i in range(0, 10):
    print clean_description_list[i]

###################################################################

train_data_features, vocab = vectorization.create_bag_of_words(clean_description_list)

print_functions.print_examples(clean_description_list, train_data_features)

print_functions.print_vocabulary(vocab)

###################################################################
