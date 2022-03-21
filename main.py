from itertools import permutations  # https://docs.python.org/3/library/itertools.html
import Dictionary

t = ''


def enter_new_word(word):
    length = len(word)
    englishWords = []
    #print(f"entered word: {word} \nwith {l} letters")
    words = []
    #print(type(words))
    for x in range(1, length + 1):
        words += (list(permutations(word, x)))  # tuples
        #print('dentro del for', words)
    words = (dict.fromkeys(words))  # trasnform to dictionary to delete duplicate
    #print('en dictionario', words)
    words = list(words.keys())  # back to list
    #print('back to list', words)
    #print(words, length)
    for y in words:
        word = (''.join(y))
        #print(word, Dictionary.Dictionary.isEnglishWord(word))  # join lists
        if Dictionary.Dictionary.isEnglishWord(word):
            englishWords.append(word)
        #print(type(word)) #son string
    return englishWords, len(englishWords), len(words)


def main(w=''):
    print("enter any word or 'exit' for exit")
    w = str.lower(input())
    if w == 'exit':
        return w
    #elif w == '':
    #    return ''
    elif w.isalpha():
        print("are english words:")
        english_words, cant_english_words, all_words = enter_new_word(w)
        print(', '.join(english_words), cant_english_words, all_words)
        return w
    else:
        print(f'{w} is not a valid word')
        return 'not valid'


if __name__ == '__main__':
    while t != 'exit':
        t = main()
    else:
        print("thanks for trying")
