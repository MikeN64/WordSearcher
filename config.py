import re

# Dictionary file
DICT_FILE = 'dictionaries/ef_3000_most_common_words_eng.txt'

# Helper Functions
def input_to_list():
    raw_letters = input('Enter letters seperated by commas:')
    letters = re.split(', ', raw_letters)
    return letters
