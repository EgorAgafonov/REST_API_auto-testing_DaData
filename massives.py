from operator import itemgetter, attrgetter
import random

# 1. Поиск совпадения в строке по шаблону (word):

# word = 'world'
# list_of_words = "the world isn't enough"
# result = list_of_words.index(word)
# print(result)
#
# if 'world' in list_of_words:
#     print(f"Слово '{word}' содержится в списке элементов.")
# else:
#     print(f"Слова '{word}' в списке элементов нет.")
#
# # 2. Объединение(распаковка - zip) значений разных списков в один словарь:
#
# keys = ['name', 'surname', 'age']
# values = ['John', 'Smith', 26]
#
# print(dict(zip(keys, values)))

# 3. Добавление и удаление ключей словаря:

# dictionary = {}
# print(id(dictionary))
# dictionary['name'] = 'Иван'
# second_dict = dictionary.copy()
# second_dict.update(surname='Павлов', age=34)
# print(dictionary)
# print(second_dict)
# del (second_dict['surname'])
# print(second_dict)

# 4. Сортировка элементов(tuple) списков, являющихся объектами созданного нами класса:

# class Capital:
#     def __init__(self, name, popul):
#         self.name = name
#         self.popul = popul
#
#     def __repr__(self):
#         return repr((self.name, self.popul))
#
#
# list_of_cap = [
#     Capital('Pekin', 2234441233),
#     Capital('Moscow', 123331233),
#     Capital('London', 300123),
#     Capital('Amsterdam', 3312333)
# ]
#
# res = sorted(list_of_cap, key=lambda capital: capital.popul, reverse=True)
# res = sorted(list_of_cap, key=attrgetter('popul'), reverse=True)
# res = sorted(list_of_cap, key=attrgetter('name'))
#
# print(res)


# 4. Сортировка словаря с различными типами данных:

# 4.1 Сортировка словаря только по ключу с помощью функции sorted:
# rooms = {"Pink": "Rm 403", "Space": "Rm 201", "Quail": "Rm 500", "Lime": "Rm 503"}
# sorted_items = sorted(rooms.items())
# sorted_items = dict(sorted_items)

# 4.2 Сортировка словаря по ключу или по значению ключа с помощью функции sorted и её аргумента key, принимающим
# анонимную lambda функцию:
# res = dict(sorted(rooms.items(), key=lambda item: item[0]))
# print(res)

# 4.3 Сортировка словаря по ключу или по значению ключа с помощью функции sorted и её аргумента key, принимающим
# функции itemgetter / attrgetter из модуля operator:
# res = dict(sorted(rooms.items(), key=itemgetter(1)))
# print(res)


# 5.1 Сортировка списка со строкой, разбитой на буквенные символы:
a = 'abcdefghijkl'
list_of_chars = list(a)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
random_chars_list = []
for i in list_of_chars:
    random_char = random.choice(list_of_chars)
    random_chars_list.append(random_char)
print(random_chars_list)
print(sorted(random_chars_list, reverse=False))

