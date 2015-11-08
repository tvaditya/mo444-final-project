__author__ = 'jose'


import nltk
#nltk.download()  # Download text data sets, including stop words

from nltk.corpus import stopwords # Import the stop word list

import re
from bs4 import BeautifulSoup

#from nltk.stem.porter import PorterStemmer
#from nltk.stem.snowball import SnowballStemmer
#from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import *
from nltk.stem import WordNetLemmatizer

import unicodedata
encoding = "utf-8"

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


#stemmer = SnowballStemmer("english")
#stemmer = PorterStemmer()
#stemmer = LancasterStemmer()
stemmer = nltk.stem.RSLPStemmer()
wnl = WordNetLemmatizer()

def clean_text( raw_text ):
    # Function to convert a raw text to a string of words
    # The input is a single string (a raw text), and
    # the output is a single string (a preprocessed text)
    #
    # 0. Includes a space before "<" to avoid joining two words together
    pre_text = raw_text.replace("<", " <")
    #
    # 0.1 Some states (such as Acre) uses "_" to separate a line
    pre_text = pre_text.replace("_", " ")
    #
    # 0.2 Removes the ordinal character: changed in the orignal file
    #pre_text = pre_text.replace(u"", " ")
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(pre_text).get_text()
    #
    # 1.5 Remove Accents
    review_text = remove_accents(review_text)
    #
    # 2. Remove non-letters
    letters_only = re.sub("[^a-zA-Z ]", " ", review_text)
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("portuguese"))
    #
    # 5. Remove stop words
    pre_meaningful_words = [w for w in words if not w in stops]
    # 5.1 
    meaningful_words = [word for word in pre_meaningful_words]
    #
    # 6. Join the words back into one string separated by space,
    # and return the result.
    return( " ".join( meaningful_words ))

