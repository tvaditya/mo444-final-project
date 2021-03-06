__author__ = 'jose'

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def create_bag_of_words(description_list):

    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.
    vectorizer = CountVectorizer(analyzer = "word",   \
                                 tokenizer = None,    \
                                 preprocessor = None, \
                                 stop_words = None)

    # fit_transform() does two functions: First, it fits the model
    # and learns the vocabulary; second, it transforms our training data
    # into feature vectors. The input to fit_transform should be a list of
    # strings.
    train_data_features = vectorizer.fit_transform(description_list)

    # Numpy arrays are easy to work with, so convert the result to an
    # array
    return train_data_features.toarray(), vectorizer.get_feature_names()


def extract_tfidf(counts):
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(counts)
    return tfidf.toarray()
