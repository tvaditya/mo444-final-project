from ada_boost import AdaBoost
from constants import *

def apply_ada_boost(filename, estimators):
    ab = AdaBoost(filename, estimators=estimators)

    #ab.split_data()
    ab.start_data()
    ab.train_ada_boost()
    ab.test_ada_boost()

    ab.switch_folds()
    ab.train_ada_boost()
    ab.test_ada_boost()


apply_ada_boost(features_directory + filename, 500)
