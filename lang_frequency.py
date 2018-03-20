import re
import collections as cll

def load_data(filepath):
    list_of_words = re.findall('\w+', open(filepath).read().lower())
    return list_of_words


def get_most_frequent_words(text):
    number_words_max_frequency = 10
    return cll.Counter(text).most_common(number_words_max_frequency)


if __name__ == '__main__':
    word_frequency = get_most_frequent_words(load_data())
    print(word_frequency)
