import pathlib
pathlib.Path()

class Dictionary:
    @staticmethod
    def isEnglishWord(wor):
        path = pathlib.Path("resources", "dictionary")
        dictionary = open(path, 'r')
        #dictionary = open(str(pathlib.Path(__file__).absolute()) + f'\\..\\resources\\dictionary', 'r')
        dictionary_list = list((dictionary.read()).split('\n'))
        if wor in dictionary_list:
            return True
        else:
            return False


