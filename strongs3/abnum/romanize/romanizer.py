#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: romanizer.py

import re

class romanizer(object):

    def __init__(self, data, add_uppercase = True):
        self.substitutes = {}
        for key, d in data.items():
            # add transliteration letter substituting greek letters
            for x in d['letter']:
                self.substitutes[x] = d['transliteration']
                if add_uppercase:
                    self.substitutes[x.upper()] = d['transliteration'].upper()
            # add the primary greek letter substituting transliteration letter
            self.substitutes[d['transliteration']] = d['letter'][0]
            if add_uppercase:
                self.substitutes[d['transliteration'].upper()] = d['letter'][0].upper()

        if len(self.substitutes):
            self.regex = re.compile('|'.join(self.substitutes.keys()))

    def preprocess(self):
        pass

    def convert(self, string, preprocess = None):
        """
        Swap characters from a script to transliteration and vice versa. 
        Optionally sanitize string by using preprocess function.

        :param preprocess:
        :param string:
        :return:
        """
        string = preprocess(string) if preprocess else string
        if self.regex:
            return self.regex.sub(lambda x: self.substitutes[x.group()], string)
        else:
            return string