import sys
import re
from collections import Counter

filepath = sys.argv[1]


def load_data(filepath):
    with open(filepath) as file:
        text = file.read().lower()
    return text


def get_most_frequent_words(text):
    list_of_words = re.findall('\w+', text)
    number_words_show = 10
    return Counter(list_of_words).most_common(number_words_show)


if __name__ == '__main__':
    word_frequency = get_most_frequent_words(load_data(filepath))
    for _ in word_frequency:
        print('слово - {} - встречается - {} - раз'.format(_[0], _[1]))
