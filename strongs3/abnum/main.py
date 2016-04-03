#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: main.py

import re
from .search import find_cumulative_indices
from . import romanize
import pandas as pd
from . import letter_value
from IPython.display import HTML
from .remarkuple import helper as h, table
from .math import digital_root, digital_sum

error_msg = "String '%s' contains unsupported characters for letter value calculation"

class AbnumException(Exception):
    pass

class Abnum(object):
    """
    from abnum import Abnum, greek
    abn = Abnum(greek)
    print abn.value('ο Λογος') -> 443
    """
    def __init__(self, code, data = None):
        self.values = {}
        self.r = romanize.__dict__[code]
        if data:
            self.data = data 
        else:
            self.data = letter_value.data[code]
        self.init_values(self.data)

    def init_values(self, data):

        values = {}

        for num, letter_code in data:
            for letter in self.r.data[letter_code]['letter']:
                # small letter value
                self.values[letter] = num
                # capital letter value
                if self.r.has_capitals:
                    self.values[letter.upper()] = num

            trans = self.r.data[letter_code]['transliteration']
            # translittered small letter value
            self.values[trans] = num
            # translittered capital letter value
            if self.r.has_capitals:
                self.values[trans.upper()] = num

        self.regex_values = re.compile('|'.join(self.values.keys()))
        self.regex_has_numbers = re.compile('\d')

    def value(self, string):
        """
        String is a greek letter, word or sentence OR roman letter representation (transliteration) 
        of the greek letter, word or sentence that will be converted to the numerical value letter by letter
        Main function will convert input to unicode format for easier frontend, but on module logic
        more straightforward function unicode_letter_value is used.
        """
        return self.unicode_value(str(string))

    def unicode_value(self, string):
        """
        String argument must be in unicode format.
        """
        result = 0
        # don't accept strings that contain numbers
        if self.regex_has_numbers.search(string):
            raise AbnumException(error_msg % string)
        else:
            num_str = self.regex_values.sub(lambda x: '%s ' % self.values[x.group()],
                                            string)
            # don't accept strings, that contains letters which haven't been be converted to numbers
            try:
                result = sum([int(i) for i in num_str.split()])
            except Exception as e:
                raise AbnumException(error_msg % string)
        return result

    def convert(self, string, sanitize=False):
        return self.r.convert(string, (self.preprocess if sanitize else False))

    def preprocess(self, string):
        return self.r.preprocess(string)

    def find(self, text, num, cumulative = False):
        words = text.split()
        numbers = list(map(self.value, words))
        if cumulative:
            result = []
            for incides in find_cumulative_indices(numbers, num):
                result.append(' '.join([words[idx] for idx in incides]))
            return result
        else:
            return [words[idx] for idx in map(numbers.index, numbers) if numbers[idx] == num]

    def char_table_data(self, text, modulo = 9):
        # initialize data dictionary, split text to columns: #, letter, translit, num, sum, mod, word
        data = dict([key, []] for key in ['letter', 'transliteration', 'value', 'word'])
        # character chart
        # split words
        for word in text.split():
            # split letters
            for idx, letter in enumerate(word):
                #data['index'].append(idx)
                data['letter'].append(letter)
                data['transliteration'].append(self.convert(letter))
                data['value'].append(self.value(letter))
                data['word'].append(word)

        data = pd.DataFrame(data)
        # word summary from character chart
        gb = data.groupby('word')
        data2 = gb.sum()
        data2['characters'] = gb['word'].apply(len)
        data2['digital_sum'] = data2['value'].apply(digital_sum)
        data2['digital_root'] = data2['value'].apply(digital_root)
        # phrase summary from word summary
        s = data2.sum()
        data3 = pd.DataFrame({'digital_root': [digital_root(s.value)],
                              'characters': [s.characters], 
                              'digital_sum': [digital_sum(s.value)],
                              'value': [s.value],
                              'phrase': text})

        return (data, data2, data3)


    def char_table(self, text, modulo = 9):
        # initialize html table
        tbl = table(Class="char-table")
        # add caption / table title
        tbl.addCaption(text)
        # add data rows
        tr1 = h.tr() # script letters
        tr2 = h.tr() # roman letters
        tr3 = h.tr() # value
        tr4 = h.tr() # summary
        i = 0
        for word in text.split():
            if i > 0:
                # add empty cells for word separation
                tr1 += h.th("&nbsp;")
                tr1 += h.th("&nbsp;")
                tr2 += h.td()
                tr2 += h.td(Class="empty-cell")
                tr3 += h.td()
                tr3 += h.td(Class="empty-cell")
                tr4 += h.td()
                tr4 += h.td()
            num = self.unicode_value(word)
            tr4 += h.td("%s %s" % (num, h.sub(digital_root(num))), colspan=len(word))
            i = i+1
            # add each letter on own cell
            for letter in word:
                tr1 += h.th(letter)
                tr2 += h.td(self.convert(letter))
                tr3 += h.td(self.unicode_value(letter))
        # add rows to table
        tbl.addHeadRow(tr1)
        tbl.addBodyRow(tr2)
        tbl.addBodyRow(tr3)
        tbl.addFootRow(tr4)
        # add summary footer for table
        num = self.unicode_value(text)
        tbl.addFootRow(h.tr(h.td("%s %s" % (num, h.sub(digital_sum(num), " / ", digital_root(num, modulo))), 
                                 colspan=len(text)+len(text.split()), 
                                 style="border-top: solid 1px #ddd")))
        return tbl
