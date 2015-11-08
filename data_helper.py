__author__ = 'jose'

import pandas as pd
import prepare_text
from constants import *

def read_csv(filename):
    csv_train = pd.read_csv(filename, header=None, delimiter=",")
    print csv_train.shape
    return csv_train

def save_file(data, directory, filename):
    data.to_csv(directory + filename, header=False, index=False)

def is_relevant(diario):
    return diario.startswith("dou") or diario.startswith("doe")

def clean_list(data):
    print "The stopwords will be removed..."
    clean_description_list = []

    print len(data)

    for i in data.index.values.tolist():
        if is_relevant(data[diario_index][i]):
            clean_description_list.append(prepare_text.clean_text(data[integra_index][i]))
        if i % 1000 == 0:
            print i
    return clean_description_list

