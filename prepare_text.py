__author__ = 'jose'

import nltk
#nltk.download()  # Download text data sets, including stop words

from nltk.corpus import stopwords # Import the stop word list

import re
from bs4 import BeautifulSoup

#from nltk.stem.snowball import SnowballStemmer
from nltk.stem import *
from nltk.stem import WordNetLemmatizer

from roman_numbers import get_roman_numbers
import brazilian_locations as bl
from months import get_months
from letters import get_letters
from law_words import get_law_words
import itertools

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

roman_numbers = get_roman_numbers()
state_initials = bl.get_state_initials()

state_names = bl.get_state_names()
state_names = [state.split() for state in state_names]
state_names = list(itertools.chain.from_iterable(state_names))

state_capitals = bl.get_state_capitals()
state_capitals = [capital.split() for capital in state_capitals]
state_capitals = list(itertools.chain.from_iterable(state_capitals))

months = get_months()
letters = get_letters()
law_words = get_law_words()

def clean_text( raw_text ):
    # Function to convert a raw text to a string of words
    # The input is a single string (a raw text), and
    # the output is a single string (a preprocessed text)
    #
    # 1. Includes a space before "<" to avoid joining two words together
    pre_text = raw_text.replace("<", " <")
    #
    # 2. Some states (such as Acre) uses "_" to separate a line
    pre_text = pre_text.replace("_", " ")
    #
    # 3. Removes the ordinal character: changed in the orignal file
    #pre_text = pre_text.replace(u"", " ")
    #
    # 4. Remove HTML
    review_text = BeautifulSoup(pre_text).get_text()
    #
    # 5. Remove Accents
    review_text = remove_accents(review_text)
    #
    # 6. Remove non-letters
    letters_only = re.sub("[^a-zA-Z ]", " ", review_text)
    #
    # 7. Convert to lower case, split into individual words
    words = letters_only.lower().split()
    #
    # 8. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("portuguese"))
    #
    # 9. Remove stop words
    meaningful_words = [w for w in words if not w in stops]
    #
    # 10. Remove the roman numbers
    meaningful_words = [w for w in meaningful_words if not w in roman_numbers]
    #
    # 11. Removing the state initials
    meaningful_words = [w for w in meaningful_words if not w in state_initials]
    #
    # 12. Removing the state names
    meaningful_words = [w for w in meaningful_words if not w in state_names]
    #
    # 13. Removing the state capital cities
    meaningful_words = [w for w in meaningful_words if not w in state_capitals]
    #
    # 14. Removing the months
    meaningful_words = [w for w in meaningful_words if not w in months]
    #
    # 15. Removing the single letters
    meaningful_words = [w for w in meaningful_words if not w in letters]
    #
    # 16. Removing law words
    meaningful_words = [w for w in meaningful_words if not w in law_words]
    #
    # 17. Removing web sites
    meaningful_words = [w for w in meaningful_words if not w.startswith("www")]
    #
    # 18. Stemmization of the words
    meaningful_words = [stemmer.stem(word) for word in meaningful_words]
    #
    # 19. Join the words back into one string separated by space,
    # and return the result.
    return( " ".join( meaningful_words ))

