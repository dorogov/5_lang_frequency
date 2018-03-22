import sys
import re
from collections import Counter


def load_data(filepath):
    with open(filepath) as file:
        text = file.read()
    return text


def get_most_frequent_words(text):
    list_of_words = re.findall('\w+', text.lower())
    number_words_showen = 10
    return Counter(list_of_words).most_common(number_words_showen)


if __name__ == '__main__':
    filepath = sys.argv[1]
    words = get_most_frequent_words(load_data(filepath))
    for token in words:
        print('слово - {} - вхождений - {}'.format(token[0], token[1]))
