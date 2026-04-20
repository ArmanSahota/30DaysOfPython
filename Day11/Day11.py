def add_two_numbers(x, y):
    return int(x) + int(y)
print(add_two_numbers('3',4))

def area_of_circle(R):
    return 3.14 * R * R
print(area_of_circle(6))

def add_all_numbers(*numbers):
    total = 0
    for i in numbers:
        if type(i) not in (int, float):
            return('Input Ints or Floats')
        total += i
    return total
print(add_all_numbers(1, 2, 3, 7, 5, 6, 7, 8, 9, 10))

def convert_celsius_to_fahrenheit(C):
    return ((C * (9/5) ) + 32)
print(convert_celsius_to_fahrenheit(4))

def check_season(Month):
    if Month.lower() in ['january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
        if Month.lower() in ['september', 'october', 'november']:
            return('Autumn')
        elif Month.lower() in ['december', 'january', 'february']:
            return('Winter')
        elif Month.lower() in ['march', 'april', 'may']:
            return('Spring')
        else:
            return('Summer')
print(check_season('SepTember'))

def calculate_slope(x1, x2, y1, y2):
    return ((y2 - y1) / (x2 - x1))

def solve_quadratic_eqn(x, a, b, c):
    return (a(x ** 2) + b(x) + c)

def print_list(arr):
    for i in arr:
        print(i)
list1 = [1, 2, 3, 4, 5, 6, 7]
print_list(list1)

def reverse_list(arr):
    L = 0
    R = len(arr) - 1
    while L < R:
        arr[L], arr[R] = arr[R], arr[L]
        L += 1
        R -= 1
    return arr
print(reverse_list(list1))
print(reverse_list(["caasdfasdf", "wertwert", "asdf"])) 

def captalize_list_items(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    return arr
print(captalize_list_items((["caasdfasdf", "wertwert", "asdf"])))

def add_item(arr, item):
    arr.append(item)
    return arr
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

def remove_item(arr, item):
    arr.remove(item)
    return arr
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

def sum_of_numbers(x):
    total = 0
    for i in range(x + 1):
        total += i
    return total
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odd(x):
    total = 0
    for i in range(x + 1):
        if i % 2 != 0:
            total += i
    return total
def sum_of_even(x):
    total = 0
    for i in range(x + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_odd(5))  # 9
print(sum_of_even(10)) # 30
print(sum_of_even(100)) # 2550

def evens_and_odds(x):
    even = 0
    odd = 0
    for i in range(x + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return (f"The number of odds are {odd} \n The number of evens are {even}")
print(evens_and_odds(100))

def factorial(x):
    total = 1
    for i in range(1, x + 1):
        total *= i 
    return total
print(factorial(10))

def is_empty(arr):
    if not arr:
        return True
    return False
print(is_empty([1]))

def greet(name = 'Guest'):
    print('Hello ', name)
greet()
greet('Arman')

def show_args(**dicts):
    string = []
    for key, val in dicts.items():
        string.append(f"{key} : {val}")
    print("received:", ", ".join(string))
print(show_args(name="Alice", age=30, city="New York"))
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny


def is_prime(x):
    for i in range(2, x + 1):
        for j in range(i, x + 1):
            if i * j == x:
                return False
    return True
print(is_prime(7))

def is_unique(arr):
    if len(set(arr)) == len(arr):
        return True
    return False
print(is_unique([1, 2, 3]))

def same_type(arr):
    type_set = set()
    for i in arr:
        type_set.add(type(i))
    return True if len(type_set) == 1 else False
print(same_type([1, 2, 3, '4']))
    
import keyword

def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)

print(is_valid_variable("my_var"))      # True
print(is_valid_variable("2cool"))       # False (cannot start with a digit)

import sys
sys.path.append('d:/30DaysOfPython')
from Day10 import countries_data
from collections import Counter

def most_spoken_languages():
    languages = set()
    languages_count = {}
    for country in countries_data.countries_data:
        for language in country['languages']:
            languages.add(language)
            if language in languages_count:
                languages_count[language] += 1
            else:
                languages_count[language] = 1
    sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)
    print(sorted_languages[:10])
most_spoken_languages()

def most_populated_countries():
    output = []
    sorted_countries = sorted(countries_data.countries_data, key= lambda x: x['population'], reverse= True)
    for c in sorted_countries[:10]:
        output.append((c['name'], c['population']))
    print(output)
most_populated_countries()


