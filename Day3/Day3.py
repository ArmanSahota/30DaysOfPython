age = 20
height = 5.07
complex_number = complex(3)

base = int(input('Enter base: '))
height = int(input('Enter height: '))
triangle = (base * height) // 2
print('The area of the triangle is', triangle)

side_a = int(input('Enter side a:'))
side_b = int(input('Enter side b:'))
side_c = int(input('Enter side c:'))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is', perimeter)
length = int(input('Enter length:'))
width = int(input('Enter width:'))
area = length * width
perimeter = (length + width) * 2
print('The area of the square is ', area)
print('The perimeter of the square is ', perimeter)

print(type('10') == 10)
print( int(9.8) == 10)

print( (7 // 3) == int(2.7))

print(len("dragon") == len("python"))
if 'on' in 'dragon' and 'on' in 'python':
    print('ON IS IN DRAGON AND PYTHON')
else:
    print(False)

string = 'python'
length = float(len(string))
string_length = str(length)
print(string_length)

number = int(input('pick a number'))
print('Your number is', 'Even' if number % 2 == 0 else 'Odd')

hours = int(input('Enter hours:'))
rate = int(input("Enter rate per hour: "))
check = hours * rate
print('Your weekly earnings are', check)

string = 'I hope this course is not full of jargon.'
if 'jargon' in string:
    print('jargon in string')
else: print('False')

radius = float(input("radius: "))
circle_area = 3.14 * radius * radius
circle_circum = 2 * 3.14 * radius
print('The area or the circle is ', circle_area)
print('The circumference of the circle is ', circle_circum)
years = int(input('Enter number of years you have lived: '))
days = 365 * years
hours = days * 24
minutes = hours * 60
secounds = minutes * 60
print('You have lived for ', secounds,  'seconds.')

print('''1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125 ''')

x1 = int(input('Enter x1'))
x2 = int(input('Enter x2'))
y1 = int(input('Enter y1'))
y2 = int(input('Enter y2'))

def slope(x1, y1, x2, y2):
    return float() (y2 - y1)/ (x2 - x1)
print('slope is ', slope(x1, y1, x2, y2))


