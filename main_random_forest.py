from random_forest import RandomForest
from constants import *

def apply_random_forest(filename):
    rf = RandomForest(filename, estimators=500)

    #rf.split_data()
    rf.start_data()
    rf.train_random_forest()
    rf.test_random_forest()

    rf.switch_folds()
    rf.train_random_forest()
    rf.test_random_forest()


apply_random_forest(features_directory + filename)
