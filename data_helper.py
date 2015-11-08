__author__ = 'jose'

import pandas as pd
import prepare_text

integra_index = 4
diario_index = 2


def read_csv(filename):
    csv_train = pd.read_csv(filename, header=None, delimiter=",")

    print csv_train.shape
    print csv_train.columns.values

    return csv_train


def is_relevant(diario):
    return diario.startswith("dou") or diario.startswith("doe")

def clean_list(data):
    print "The stopwords will be removed and the remaining words will be stemmized..."
    clean_description_list = []

    print len(data)

    for i in data.index.values.tolist():
        if is_relevant(data[diario_index][i]):
            clean_description_list.append(prepare_text.clean_text(data[integra_index][i]))
        if i % 1000 == 0:
            print i
    return clean_description_list

