import re

def load_data(filepath):
    with open('filepath', 'r') as f:
        d = f.read() #читаем файл целиком
    d = re.split(r'[\d\W+]', d) # разделяем текст рек выражением - разделители все что не буквы
    d = [token.lower() for token in d]# приводим все к нижнему регистру
    s = {}
    for elem in d:# создаем словарь из слов в списке - ключ и количествоих в тексте - значение
        s[elem] = s.get(elem, 0) + 1
    t = []
    for key in sorted(s):# создаем сортированный список списков - слово,количество попаданий
        t.append([key, s[key]])
    return t


def get_most_frequent_words(text):
    10_words = sorted(text, key=lambda x: x[1], reverse=True)
    del 10_words[0]
    return 10_words[:10]


if __name__ == '__main__':
    g = get_most_frequent_words(load_data())
    print(g)
