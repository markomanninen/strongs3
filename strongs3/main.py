#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: main.py

import re
import pandas as pd
from os.path import isfile
from .abnum import greek, hebrew, Abnum

dictionary = None

def greek_find(query=None, column=None):
    result = find(query, column)
    return result[result['lemma'].str.contains('^G')]

def hebrew_find(query=None, column=None):
    result = find(query, column)
    return result[result['lemma'].str.contains('^H')]

greek.find = greek_find
hebrew.find = hebrew_find

def load_dictionary(mappings = {'greek': None, 'hebrew': None}, csv = None):
    
    global dictionary

    import os

    if csv is None:
        d = os.path.dirname(os.path.abspath(__file__))
        csv = "%s/strongs.csv" % d
    
    if isfile(csv):

        print ("Retrieving Strong's data from local csv copy (%s) ..." % csv)
        
        dictionary = pd.read_csv(csv, sep = ",")
        
        mappings['greek'] = mappings['greek'] if 'greek' in mappings else None
        g = Abnum(greek, mappings['greek'] if mappings['greek'] else {})

        greek_dictionary = dictionary[dictionary['lemma'].str.contains(r'^G')].copy()
        # greek words are preprocessed to discard accents
        greek_dictionary['word'] = greek_dictionary['word'].map(lambda x: g.preprocess(x))
        # adding transliteration of the words to the dataframe
        greek_dictionary['transliteration'] = greek_dictionary['word'].map(lambda x: g.convert(x))
        # adding word isopsephy/gematria value to the dataframe
        greek_dictionary['abnum'] = greek_dictionary['word'].map(lambda x: g.value(x))
        # adding word isopsephy value to the dataframe
        greek_dictionary['word_len'] = greek_dictionary['word'].map(lambda x: len(x))
        
        mappings['hebrew'] = mappings['hebrew'] if 'hebrew' in mappings else None
        h = Abnum(hebrew, mappings['hebrew'] if mappings['hebrew'] else {})

        hebrew_dictionary = dictionary[dictionary['lemma'].str.contains(r'^H')].copy()
        # hebrew words are preprocessed to discard accents
        hebrew_dictionary['word'] = hebrew_dictionary['word'].map(lambda x: h.preprocess(x))
        # adding transliteration of the words to the dataframe
        hebrew_dictionary['transliteration'] = hebrew_dictionary['word'].map(lambda x: h.convert(x))
        # adding word isopsephy/gematria value to the dataframe
        hebrew_dictionary['abnum'] = hebrew_dictionary['word'].map(lambda x: h.value(x))
        # adding word isopsephy value to the dataframe
        hebrew_dictionary['word_len'] = hebrew_dictionary['word'].map(lambda x: len(x))

        dictionary = pd.concat([greek_dictionary, hebrew_dictionary])

    else:
        print ("Cannot read Strong's csv file: %s! Please check path/filename and reload dictionary with load_dataframe(csv = \"your_filename\") function" % csv)

def find(query, column):
    global dictionary
    if not query:
        return dictionary
    # if column is "abnum" or "word_len" use == for int comparison
    return dictionary[dictionary[column] == query] if column == 'abnum' else dictionary[dictionary[column].str.contains(query)]
