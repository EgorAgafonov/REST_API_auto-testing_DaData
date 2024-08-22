from operator import itemgetter, attrgetter

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

# dictionary = {}
# print(id(dictionary))
# dictionary['name'] = 'Иван'
# second_dict = dictionary.copy()
# second_dict.update(surname='Павлов', age=34)
# print(dictionary)
# print(second_dict)
# del (second_dict['surname'])
# print(second_dict)


class Capital:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return repr((self.name, self.population))


population = [('Pekin', 2234441233), ('Moscow', 123331233), ('London', 300123), ('Amsterdam', 3312333)]
res = sorted(population, key=lambda capital: capital[1], reverse=True)

# res = sorted(population, key=attrgetter('value'))
print(res)
