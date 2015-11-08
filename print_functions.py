__author__ = 'jose'

def print_vocabulary(vocab):
    print "Vocabulary (size: " + str(len(vocab)) + "): "
    #print vocab


def print_examples(clean_description, train_data_features, size = 10):

    print "Feature Shape: " + str(train_data_features.shape)
    print("\nExamples of the features:")

    for i in range(0, size):
        print(i)
        print(clean_description[i])
        print(train_data_features[i])
        print("\n")

