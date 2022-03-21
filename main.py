from itertools import permutations  # https://docs.python.org/3/library/itertools.html
import Dictionary

t = ''


def enter_new_word(word):
    length = len(word)
    englishWords = []
    words = []
    for x in range(1, length + 1):
        words += (list(permutations(word, x)))  # tuples
    words = (dict.fromkeys(words))  # trasnform to dictionary to delete duplicate
    words = list(words.keys())  # back to list
    for y in words:
        word = (''.join(y))
        if Dictionary.Dictionary.isEnglishWord(word):
            englishWords.append(word)
    return englishWords, len(englishWords), len(words)


def main(w=''):
    print("enter any word or 'exit' for exit")
    w = str.lower(input())
    if w == 'exit':
        return w
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
