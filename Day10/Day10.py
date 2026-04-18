#level 1
for i in range(10):
    print(i)
i = 0
while i != 11:
    print(i)
    i += 1

for i in range(10, 0, -1):
    print(i)
i = 10
while i != 0:
    print(i)
    i -= 1

for i in range(8):
    print(i * '#')

for i in range(9):
    print('# # # # # # # #')

for i in range(11):
    print(f"{i} X {i} = {i * i}")

Libraries_list =  ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in Libraries_list:
    print(i)

for i in range(0, 101):
    print(i) if i % 2 == 0 else None
for i in range(0, 101):
    print(i) if i % 2 != 0 else None


#level 2
num = 0
for i in range(0, 101):
    num += i
print(f"The sum of all numbers is {num}")

even_num = 0
odd_num = 0
for i in range(0, 101):
    if i % 2 == 0:
        even_num += i
    else:
        odd_num += i
print(f"The sum of all even numbers is {even_num}")
print(f"The sum of all odd numbers is {odd_num}")

#Level 3
import sys
sys.path.append('d:/30DaysOfPython')
from Day5 import countries
for country in countries.countries:
    if 'land' in country.lower():
        print(country)
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = []
for i in range(len(fruits)-1, -1, -1):
    new_fruit.append(fruits[i])
print (new_fruit)

from collections import Counter
from countries_data import countries_data
languages = set()
languages_count = {}
for country in countries_data:
    for language in country['languages']:
        languages.add(language)
        if language in languages_count:
            languages_count[language] += 1
        else:
            languages_count[language] = 1
sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)

for lang, count in sorted_languages[:10]:
    print(lang, count)

sorted_countries = sorted(countries_data, key= lambda x: x['population'], reverse= True)

for c in sorted_countries[:10]:
    print(c['name'], c['population'])







