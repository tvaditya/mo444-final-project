__author__ = 'jose'

from sklearn.feature_extraction.text import CountVectorizer

def create_bag_of_words(description_list):

    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.
    vectorizer = CountVectorizer(analyzer = "word",   \
                                 tokenizer = None,    \
                                 preprocessor = None, \
                                 stop_words = None)#,   \
                                 #max_features = 5000)

    # fit_transform() does two functions: First, it fits the model
    # and learns the vocabulary; second, it transforms our training data
    # into feature vectors. The input to fit_transform should be a list of
    # strings.
    train_data_features = vectorizer.fit_transform(description_list)

    # Numpy arrays are easy to work with, so convert the result to an
    # array
    return train_data_features.toarray(), vectorizer.get_feature_names()

