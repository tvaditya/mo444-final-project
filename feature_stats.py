__author__="jose"

from constants import *
import data_helper as dh


def print_stats(source_file, columns):
    csv_features = dh.read_csv(source_file)

    size_entries = len(csv_features)
    entries = csv_features.groupby(columns)

    for name, group in entries:
        print "Group Name: " + str(name)
        entry = len(group)
        print entry / float(size_entries)


print_stats(features_directory + filename, [0])
print_stats(clean_text_directory + filename, [diario_index])
