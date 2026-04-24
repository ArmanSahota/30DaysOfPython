#Map goes through a list and maps the functions value for 
# each item in the list and returns a list of each item after the funcitons
#filter uses booleans and keeps the True values and returns those in the return list
#reduce returns single value after doing the funciton to the list

#closure is when a nested function has outer scope of the enclosing function meaning you 
# make a function and add a variable to the functions and use that variable inside the nested function

#DECORATOR is using an outer funtion with a wraper inside. Then we use it by doing @decorator 
# before the function we use. 

#higher order function is returning a different function based on different parameters
 
def index_to_string(x):
    return x.upper()

caps = (map(index_to_string,['Asabeneh', 'Lidiya', 'Ermias', 'Abraham', 'ARMAN'])) 
print(list(caps))

def is_even(x):
    return True if x % 2 == 0 else False
even = filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 1234])
print(list(even))
from functools import reduce
def subtract_two_numbers(x, y):
    return x - y
subtraction = reduce(subtract_two_numbers, [100, 2, 3, 4 ,5, 6, ])
print(subtraction)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in countries:
    print(i)

for i in names:
    print(i)

for i in numbers:
    print(i)
countries_caps = map(index_to_string, countries)
print(list(countries_caps))

def square(x):
    return x ** 2
squared_numbers = map(square, numbers)
print(list(squared_numbers))
name_caps = map(index_to_string, names)
print(list(name_caps))

def land_removal(x):
    return False if 'land' in x else True
land_delete = filter(land_removal, countries)
print(list(land_delete))

def six_char(x):
    return False if len(x) == 6 else True
six_deletion = filter(six_char, countries)
print(list(six_deletion))
def over_six_char(x):
    return False if len(x) >= 6 else True
six_deletion = filter(over_six_char, countries)
print(list(six_deletion))

def E_delete(x):
    return False if x[0] == 'E' else True
E_remove = filter(E_delete, countries)
print(list(E_remove))


result = reduce(lambda x, y: x + y, filter(lambda n : n % 2 == 0, map(lambda n : n ** 2, numbers)))
print(result)
numbers = [1, 2, '3', 4, 5, 6, 7, 8, '9', 10]
def get_string_list(arr):
    result = filter(lambda x: type(x) == str, arr )
    return list(result)
print(get_string_list(numbers))
print(reduce(lambda x, y : int(x) + int(y), numbers ))

concatenated = reduce(lambda x, y: x + ', ' + y, countries)
last_comma = concatenated.rfind(',')
sentence = (concatenated[:last_comma]+ ', and' + concatenated[last_comma + 1: ] + ' are north European countries')

print(sentence)
import sys
sys.path.append('d:/30DaysOfPython')
from Day5 import countries

def LandSearch(x):          # a square function
    land = filter(lambda y: 'land' in y.lower(), x)
    return list(land)

def Ia_search(x):            # a cube function
    ia = filter(lambda y : 'ia' in y.lower(), x)
    return list(ia)

def island_search(x):        # an absolute value function
    island = filter(lambda y: 'island' in y.lower(), x)
    return list(island)

def higher_order_function(type): # a higher order function returning a function
    if type == 'land':
        return LandSearch
    elif type == 'ia':
        return Ia_search
    elif type == 'island':
        return island_search

result = higher_order_function('island')
print(result(countries.countries))   
result = higher_order_function('ia')
print(result(countries.countries))
result = higher_order_function('land')
print(result(countries.countries))      


def country_count(arr):
    count = {}
    for x in arr:
        key = x[0]
        count[key] = 1 + count.get(key, 0)
    return count
print(country_count(countries.countries))

def first_ten_countries(arr):
    return arr[ : 11]
print(first_ten_countries(countries.countries))

def last_ten_countries(arr):
    return arr[-10 :]
print(last_ten_countries(countries.countries))

from Day10 import countries_data

def sort_country(arr):
    # Sort by name
    by_name = sorted(arr, key=lambda x: x['name'])
    print("Sorted by name:")
    for c in by_name[:10]:
        print(f"  {c['name']}")
    
    # Sort by capital
    by_capital = sorted(arr, key=lambda x: x['capital'])
    print("\nSorted by capital:")
    for c in by_capital[:10]:
        print(f"  {c['capital']} - {c['name']}")
    
    # Sort by population (descending)
    by_population = sorted(arr, key=lambda x: x['population'], reverse=True)
    print("\nSorted by population:")
    for c in by_population[:10]:
        print(f"  {c['name']}: {c['population']:,}")
    
    return by_name, by_capital, by_population

# Sort countries by name, capital, population
sort_country(countries_data.countries_data)

# Ten most spoken languages
def most_spoken_languages(arr, n=10):
    language_count = {}
    for country in arr:
        for lang in country.get('languages', []):
            language_count[lang] = language_count.get(lang, 0) + 1
    
    # Sort by count (descending) and return top n
    sorted_langs = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    print(f"\nTop {n} most spoken languages:")
    for lang, count in sorted_langs[:n]:
        print(f"  {lang}: {count} countries")
    return sorted_langs[:n]

most_spoken_languages(countries_data.countries_data)

# Ten most populated countries
def most_populated_countries(arr, n=10):
    sorted_countries = sorted(arr, key=lambda x: x['population'], reverse=True)
    print(f"\nTop {n} most populated countries:")
    for c in sorted_countries[:n]:
        print(f"  {c['name']}: {c['population']:,}")
    return sorted_countries[:n]

most_populated_countries(countries_data.countries_data)


def higher_order_function(type): # a higher order function returning a function
    if type == 'land':
        return LandSearch
    elif type == 'ia':
        return Ia_search
    elif type == 'island':
        return island_search

result = higher_order_function('island')
print(result(countries.countries))   
result = higher_order_function('ia')
print(result(countries.countries))
result = higher_order_function('land')
print(result(countries.countries))      
