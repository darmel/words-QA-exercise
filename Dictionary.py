import pathlib
import os
import sys


class Dictionary:
    @staticmethod
    def isEnglishWord(wor):
        path = pathlib.Path("resources", "dictionary")
        PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(PROJECT_ROOT,path)
        dictionary = open(path, 'r')
        dictionary_list = list((dictionary.read()).split('\n'))
        if wor in dictionary_list:
            return True
        else:
            return False


