# Что делает

Данный модуль предназначен для нахождения 10 наиболее встречающихся слов в заданном тексте с указанием количества вхождений слова в текст.

# Как делает
1. Импортируем необходимые библиотеки

```#!powershell
import sys # для считывания имени пути из терминала
import re # для работы с регулярными выражениями, подробнее далее по тексту
from collections import Counter # для подсчета количества вхождений слов
```

- в терминале: 
```#!powershell
>>> ... python3 lang_frequency.py /.../hamlet.txt

```

2. функция открывающая файл и считывающая его
```#!powershell
def load_data(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

```

3. фукция определяющую 10 наиболее часто встречающихся слов с указанием сколько раз они встречатся
```#!powershell
def load_data(filepath):
    with open(filepath) as file:
        text = file.read()
    return text
```
4. Выводим значение в терминал
```#!powershell
if __name__ == '__main__':
    filepath = sys.argv[1]
    words = get_most_frequent_words(load_data(filepath))
    for token in words:
        print('слово - {} - встречается - {} - раз'.format(token[0], token[1]))

```
пример:
```
- в терминале: 
```#!powershell
>>> ... python3 lang_frequency.py /.../hamlet.txt

```
вывод:
```
- в терминале: 
```#!powershell
слово - и - вхождений - 1879
слово - в - вхождений - 1599
слово - не - вхождений - 969
слово - что - вхождений - 911
слово - гамлет - вхождений - 670
слово - он - вхождений - 550
слово - с - вхождений - 534
слово - как - вхождений - 530
слово - на - вхождений - 467
слово - его - вхождений - 462
```
