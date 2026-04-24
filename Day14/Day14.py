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


