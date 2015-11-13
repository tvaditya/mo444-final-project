from random_forest import RandomForest
from constants import *

def apply_random_forest(filename):
    rf = RandomForest(filename)

    #rf.split_data()
    rf.start_data()
    rf.train_random_forest()
    rf.test_random_forest()

    rf.switch_folds()
    rf.train_random_forest()
    rf.test_random_forest()



filename = features_directory + "out-july-2015-dou.out"
apply_random_forest(filename)
