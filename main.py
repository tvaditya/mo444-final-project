__author__ = 'jose'

import pandas as pd
import print_functions, vectorization, data_helper#, tfidf
from constants import *

train_size = 1000 # 15000

filename = "out-july-2015-dou.out"

def clean_text():
    csv = data_helper.read_csv(raw_directory + filename)

    # Slice the data to get the training data
    train = csv[:][:train_size]

    clean_description_list = data_helper.clean_list(train)
    train[integra_index] = clean_description_list
    data_helper.save_file(train, filename)

def perform_vectorization():
    csv = data_helper.read_csv(clean_text_directory + filename)
    clean_description_list = csv[integra_index][:train_size]
    train_data_features, vocab = vectorization.create_bag_of_words(clean_description_list)
    print_functions.print_examples(clean_description_list, train_data_features)
    print_functions.print_vocabulary(vocab)


print "Train size: " + str(train_size)
clean_text()
perform_vectorization()
