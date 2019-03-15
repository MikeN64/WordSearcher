import re
import WordSearcher
import config

def regular_mode(words):
    letter = input('Enter starting letter:')
    start_words = WordSearcher.start_with(letter, words)
    return start_words

def as_ban_mode(words):
    letter = input('Enter starting letter:')
    start_words = WordSearcher.start_with(letter, words)
    result = WordSearcher.ban_letters(['a', 's'], start_words)
    return result

def nrt_ban_mode(words):
    letter = input('Enter starting letter:')
    start_words = WordSearcher.start_with(letter, words)
    result = WordSearcher.ban_letters(['n', 'r', 't'], start_words)
    return result

def random_ban_mode(words):
    letter = input('Enter starting letter:')
    start_words = WordSearcher.start_with(letter, words)
    letters = config.input_to_list()
    result = WordSearcher.ban_letters(letters, start_words)
    return result

if __name__ == '__main__':
    # get dictionary
    words = WordSearcher.load_words(config.DICT_FILE)
    
    # set word length restriction to 23
    max_length = 23
    
    # Dictionary of modes
    modes = {
            1 : regular_mode,
            2 : as_ban_mode,
            3 : nrt_ban_mode,
            4 : random_ban_mode
            }

    # User select mode
    print('Select a mode to search words with')
    for key in modes:
        print(str(key) + ': ' + modes[key].__name__)
    
    mode = int(input('Mode: '))
    if mode not in range(1, len(modes) + 1):
        print('Invalid mode')
        pass

    is_finished = False
    while not is_finished:
        result = modes[mode](words)
        result = WordSearcher.sort_words_by(len, result)
        for word in result:
            if len(word) <= max_length:
                print(word)
        
        if input('\nContinue? (Y/N): ').upper() != 'Y':
            is_finished = True
