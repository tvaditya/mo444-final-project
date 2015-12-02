from constants import *

def apply_svm_model(filename):
    sm = SvmModel(filename, estimators=500)

    #rf.split_data()
    sm.start_data()
    sm.train_svm_model()
    sm.test_svm_model()

    sm.switch_folds()
    sm.train_svm_model()
    sm.test_svm_model()


apply_svm_model(features_directory + filename)
