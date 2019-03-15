import re

def search_words(requirements):
    for requirement in requirements:
        pass

def ban_letters(letters, words):
    if letters == []:
        return words
    
    result = []
    letter = letters.pop()
    for word in words:
        if letter not in word:
            result.append(word)

    return ban_letters(letters, result)


def start_with(letter, words):
    result = []
    pattern = r'' + letter + '.'
    for word in words:
        if re.match(pattern, word):
            result.append(word)
    return result

def load_words(dict_file):
    with open(dict_file) as word_file:
        words = set(word_file.read().split())
    
    return words

def contain(letters):
    pass

def only_contain(letters):
    pass

def sort_words_by(key, words, is_reverse=False):
    words.sort(key=key, reverse=is_reverse)
    return words
