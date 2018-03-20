import re
import collections as cll

def load_data(filepath):
    data = re.findall('\w+', open(filepath).read().lower())
    return data


def get_most_frequent_words(text):
    return cll.Counter(text).most_common(10)


if __name__ == '__main__':
    g = get_most_frequent_words(load_data())
    print(g)
