numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in numbers if i <1]
print(negative_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list_numbers = [i for row in list_of_lists for i in row]
print(list_numbers)

list_of_tuples = [(i, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flatten_list = [[x, x[:3].upper(), y] for i in countries for x, y in i]
print(flatten_list)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dictionary_list = [{'country' : x, 'city' : y} for i in countries for x, y in i]
print(dictionary_list)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
fullnames = [f"{x} {y}" for i in names for x, y in i]
print(fullnames)

slope = lambda x1, x2, y1, y2:(y2 - y1)/ (x2 - x1)
print(slope(5, 7, 2, 4))