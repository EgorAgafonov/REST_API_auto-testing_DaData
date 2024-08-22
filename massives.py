# 'the largest world', "world's famous toy"

# word = 'world'
# list_of_words = "the world isn't enough"
# result = list_of_words.index(word)
# print(result)
# if 'world' in list_of_words:
#     print(f"Слово '{word}' содержится в списке элементов.")
# else:
#     print(f"Слова '{word}' в списке элементов нет.")

# keys = ['name', 'surname', 'age']
# values = ['John', 'Smith', 26]
# print(dict(zip(keys, values)))

dictionary = {}
print(id(dictionary))
dictionary['name'] = 'Иван'
second_dict = dictionary.copy()
second_dict.update(surname='Павлов', age=34)
print(dictionary)
print(second_dict)
