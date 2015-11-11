__author__ = 'jose'

import pandas as pd
import print_functions, vectorization, data_helper#, tfidf
from constants import *

size = 1000 # 15000

filename = "out-july-2015-dou.out"

def clean_text():
    csv = data_helper.read_csv(raw_directory + filename)

    # Slice the data to clean the text
    data = csv[:][:size]

    clean_description_list = data_helper.clean_list(data)
    data[integra_index] = clean_description_list
    data_helper.save_file(data, clean_text_directory, filename)

def perform_vectorization():
    csv = data_helper.read_csv(clean_text_directory + filename)
    corpus = csv[integra_index][:size]
    data_features, vocab = vectorization.create_bag_of_words(corpus)
    print_functions.print_examples(corpus, data_features)
    print_functions.print_vocabulary(vocab)

    df_data_features = pd.DataFrame(data_features)
    data = pd.DataFrame(csv)
    data = data[data.columns.values[:-1]]

    new_columns = ["interesse", "exclusao", "diario", "tipo_ato"]
    original_columns = data.columns.values
    for i in range(0, len(original_columns)):
        data[new_columns[i]] = data[original_columns[i]]

    data = data[new_columns]
    new_data = data.join(df_data_features)
    data_helper.save_file(new_data, features_directory, filename)


print "Train size: " + str(size)
clean_text()
perform_vectorization()
