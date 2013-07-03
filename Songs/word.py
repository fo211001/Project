#-*- coding: utf-8 -*-
from syllable import Syllable


class Word(object):
    def __init__(self, word):
        listSyllables = []
        tempStr = ""
        for i in word:
            if i in "аеёиоуыэюя":
                tempStr += i
                listSyllables.append(Syllable(tempStr))
                tempStr = ""
            else:
                tempStr += i
                if i == word[-1] or i == '-':
                    listSyllables[-1] += tempStr
                    tempStr = ""
        for j in listSyllables:
            print j
        self.syllable = listSyllables
