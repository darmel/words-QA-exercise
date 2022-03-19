from itertools import permutations  # https://docs.python.org/3/library/itertools.html
import Dictionary

t = ''


def enter_new_word(word):
    l = len(word)
    englishWords = []
    #print(f"entered word: {word} \nwith {l} letters")
    words = []
    #print(type(words))
    for x in range(1, l + 1):
        words += (list(permutations(word, x)))  # tuples
    words = (dict.fromkeys(words))  # trasnform to dictionary to delete duplicate
    words = list(words.keys())  # back to list
    for y in words:
        word = (''.join(y))
        #print(word, Dictionary.Dictionary.isEnglishWord(word))  # join lists
        if Dictionary.Dictionary.isEnglishWord(word):
            englishWords.append(word)
        #print(type(word)) #son string
    return englishWords


def main():
    print("enter any word or 'exit' for exit")
    w = str.lower(input())
    if w == 'exit':
        return w
    elif w == '':
        return ''
    elif w.isalpha():
        print("are english words:")
        print(', '.join(enter_new_word(w)))
        return w
    else:
        print(f'{w} is not a valid word')
        return 'not valid'


if __name__ == '__main__':
    while t != 'exit':
        t = main()
    else:
        print("thanks for trying")
