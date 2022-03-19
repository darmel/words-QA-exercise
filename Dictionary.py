class Dictionary:
    @staticmethod
    def isEnglishWord(wor):
        dictionary = open('C:\\Users\\Darmel\\PycharmProjects\\words-QA-exercise\\resources\\dictionary', 'r')
        dictionary_list = list((dictionary.read()).split('\n'))
        if wor in dictionary_list:
            return True
        else:
            return False


