__author__ = 'jose'

import pandas as pd
import print_functions, vectorization, data_helper#, tfidf
from constants import *
from law_words import get_termos_interesse
import numpy as np

size = 10000 # 15000

threshold = 0.001

def clean_text(publicacao = "", remove_excluidas = True):
    csv = data_helper.read_csv(raw_directory + filename)

    # Filter the "publicacao/diario"
    if publicacao != "":
        criterion = csv[diario_index].map(lambda x: x.startswith(publicacao))# or x.startswith('doe-sp'))
        csv = csv[criterion]

    # Filter the "regras de exclusao"
    if remove_excluidas:
        csv = csv[csv[regra_exclusao_index] == 0]

    # Slice the data to clean the text
    data = csv[:][:size]

    clean_description_list = data_helper.clean_list(data)
    data[integra_index] = clean_description_list

    data_helper.save_file(data, clean_text_directory, filename)

def perform_vectorization():
    csv = data_helper.read_csv(clean_text_directory + filename)
    corpus = csv[integra_index][:size]
    counts, vocab = vectorization.create_bag_of_words(corpus)
    print_functions.print_examples(corpus, counts)
    print_functions.print_vocabulary(vocab)

    data_features = vectorization.extract_tfidf(counts)
    df_data_features = pd.DataFrame(data_features, columns=vocab)
    columns_to_keep = []
    termos_interesse = get_termos_interesse()

    print "Total Columns: " + str(len(df_data_features.columns))
    for column in df_data_features.columns:
        if np.mean(df_data_features[column]) > threshold or column in termos_interesse:
            columns_to_keep.append(column)
    df_data_features = df_data_features[columns_to_keep]
    print "Columns to Keep: " + str(len(columns_to_keep))

    data = pd.DataFrame(csv)
    data = data[data.columns.values[:-1]]

    new_columns = ["interesse"]#, "exclusao", "diario", "tipo_ato"]
    original_columns = data.columns.values
    for i in range(0, len(new_columns)):
        data[new_columns[i]] = data[original_columns[i]]

    data = data[new_columns]
    new_data = data.join(df_data_features)
    data_helper.save_file(new_data, features_directory, filename)


print "Train size: " + str(size)
clean_text(publicacao = "dou")
perform_vectorization()
