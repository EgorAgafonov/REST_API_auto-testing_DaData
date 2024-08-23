from operator import itemgetter, attrgetter

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

# 4. Сортировка элементов списков, являющихся объектами созданного нами класса:

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

rooms = {"Pink": "Rm 403", "Space": "Rm 201", "Quail": "Rm 500", "Lime": "Rm 503"}
sorted_items = sorted(rooms.items())
res = dict(sorted_items)
print(res)
