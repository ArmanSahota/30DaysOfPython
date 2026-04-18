#Level 1
age = int(input('Enter your age: '))
if age < 18:
    print(f'You need {18 - age} more years to learn to drive')
else:
    print('You are old enough to drive.')
my_age = 20

if age == my_age:
    print('Hey we are twins!')
elif age > my_age + 1:
    print(f'You are {age - my_age} older than me.')
elif age < my_age - 1:
    print(f'You are {my_age - age} younger than me.')
else:
    if age == my_age + 1:
        print('You are a year older than me.')
    else:
        print('You are a year younger than me.')

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')


#Level 2
Score = int(input('Enter you score: '))
if Score > 90:
    print('A')
elif Score > 80:
    print('B')
elif Score > 70:
    print('C')
elif Score > 60:
    print('D')
else:
    print('F')

month = input('Pick a month: ')

if month in ['September', 'October', 'November']:
    print('Autumn')
elif month in ['December', 'January', 'February']:
    print('Winter')
elif month in ['March', 'April', 'May']:
    print('Spring')
else:
    print('Summer')

fruits = ['banana', 'orange', 'mango', 'lemon']
my_fruit = input('Pick a fruit: ')

if my_fruit not in fruits:
    fruits.append(my_fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')


#Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if person['skills']:
    middle = len(person['skills']) //2
    print(person['skills'][middle])
    if 'Python' in person['skills']:
        print(f"{person['first_name']} also knows Python")

if set(person['skills']) == {'JavaScript', 'React'} :
    print('They are a front end developer')
elif 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    if 'Python' in person['skills']:
        print('They are a backend developer')
    elif 'React' in person['skills']:
        print('They are a fullstack developer')
else:
    print('Unknown title')

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. They are married")
    
   

