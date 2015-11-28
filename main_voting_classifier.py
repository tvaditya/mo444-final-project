from voting_classifier import VotingClassifier
from constants import *

def apply_classifier(filename):
    classifier = VotingClassifier(filename)

    #rf.split_data()
    classifier.start_data()
    classifier.train()
    classifier.test()

    classifier.switch_folds()
    classifier.train()
    classifier.test()


apply_classifier(features_directory + filename)
