#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: eng.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = True

data = OrderedDict()

data['a'] = dict(letter=[u'a'], name=u'αλφα', segment='vowel', subsegment='short', transliteration=u'a', order=1)
data['b'] = dict(letter=[u'b'], name=u'βητα', segment='consonant', subsegment='mute', transliteration=u'b', order=2)
data['c'] = dict(letter=[u'c'], name=u'γαμμα', segment='consonant', subsegment='mute', transliteration=u'c', order=3)
data['d'] = dict(letter=[u'd'], name=u'δελτα', segment='consonant', subsegment='mute', transliteration=u'd', order=4)
data['e'] = dict(letter=[u'e'], name=u'ε ψιλον', segment='vowel', subsegment='short', transliteration=u'e', order=5)
data['f'] = dict(letter=[u'f'], name=u'διγαμμα', segment='numeral', subsegment='', transliteration=u'f', order=6)
data['g'] = dict(letter=[u'g'], name=u'ζητα', segment='consonant', subsegment='double', transliteration=u'g', order=7)
data['h'] = dict(letter=[u'h'], name=u'ητα', segment='vowel', subsegment='long', transliteration=u'h', order=8)
data['i'] = dict(letter=[u'i'], name=u'θητα', segment='consonant', subsegment='mute', transliteration=u'i', order=9)
data['j'] = dict(letter=[u'j'], name=u'ιωτα', segment='vowel', subsegment='short', transliteration=u'j', order=10)
data['k'] = dict(letter=[u'k'], name=u'καππα', segment='consonant', subsegment='mute', transliteration=u'k', order=11)
data['l'] = dict(letter=[u'l'], name=u'λαμβδα', segment='consonant', subsegment='semivowel', transliteration=u'l', order=12)
data['m'] = dict(letter=[u'm'], name=u'μυ', segment='consonant', subsegment='semivowel', transliteration=u'm', order=13)
data['n'] = dict(letter=[u'n'], name=u'νυ', segment='consonant', subsegment='semivowel', transliteration=u'n', order=14)
data['o'] = dict(letter=[u'o'], name=u'ξει', segment='consonant', subsegment='double', transliteration=u'o', order=15)
data['p'] = dict(letter=[u'p'], name=u'ο μικρον', segment='vowel', subsegment='short', transliteration=u'p', order=16)
data['q'] = dict(letter=[u'q'], name=u'πει', segment='consonant', subsegment='mute', transliteration=u'r', order=17)
data['r'] = dict(letter=[u'r'], name=u'κοππα', segment='numeral', subsegment='', transliteration=u'r', order=18)
data['s'] = dict(letter=[u's'], name=u'ρω', segment='consonant', subsegment='semivowel', transliteration=u's', order=19)
data['t'] = dict(letter=[u't'], name=u'σιγμα', segment='consonant', subsegment='semivowel', transliteration=u't', order=20)
data['u'] = dict(letter=[u'u'], name=u'ταυ', segment='consonant', subsegment='mute', transliteration=u'u', order=21)
data['v'] = dict(letter=[u'v'], name=u'υ ψιλον', segment='vowel', subsegment='short', transliteration=u'v', order=22)
data['w'] = dict(letter=[u'w'], name=u'φει', segment='consonant', subsegment='mute', transliteration=u'w', order=23)
data['x'] = dict(letter=[u'x'], name=u'χει', segment='consonant', subsegment='mute', transliteration=u'x', order=24)
data['y'] = dict(letter=[u'y'], name=u'ψει', segment='consonant', subsegment='double', transliteration=u'y', order=25)
data['z'] = dict(letter=[u'z'], name=u'ω μεγα', segment='vowel', subsegment='long', transliteration=u'z', order=26)

r = romanizer(data)

# collect letters from data dictionary for preprocessing function
letters = ''.join(data.keys())
regex = re.compile('[^%s ]+' % letters)

def preprocess(string):
    """
    Preprocess string to transform all diacritics and remove other special characters
    
    :param string:
    :return:
    """
    return regex.sub('', string)

def convert(string, sanitize=False):
    """
    Swap characters from script to transliterated version and vice versa.
    Optionally sanitize string by using preprocess function.
    
    :param sanitize:
    :param string:
    :return:
    """
    return r.convert(string, (preprocess if sanitize else False))