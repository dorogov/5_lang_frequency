import sys
import os
import re
from collections import Counter
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as file:
        text = file.read()
    return text



def get_most_frequent_words(text):
    list_of_words = re.findall('\w+', text.lower())
    number_words_showen = 10
    return Counter(list_of_words).most_common(number_words_showen)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, metavar='ФАЙЛ',
                        help='Путь до текстового файла.')
    namespace = parser.parse_args()
    data = load_data(namespace.file)
    ten_words = get_most_frequent_words(data)
    for key, item in ten_words:
        print('слово - {} - вхождений - {}'.format(key, item))
