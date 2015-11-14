__author__="jose"

from constants import *
import data_helper as dh


filename = features_directory + "out-july-2015-dou.out"
csv_features = dh.read_csv(filename)

size_entries = csv_features.shape[0]
entries = csv_features.groupby([0])

for i in range(0, len(entries.size())):
    entry = entries.size()[i]
    print entry / float(size_entries)

