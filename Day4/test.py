thirty = 'Thirty '
days = 'Days '
_of = 'Of '
_python = 'Python'
concatenation = thirty + days + _of + _python
print(concatenation)
coding = 'coding'
_for  = 'for'
_all = 'all'
print('{} {} {}'.format(coding, _for, _all))
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.swapcase())
print(company.title())

print('coding' in company)

print(company.replace('coding', 'python'))
p_for_all = 'Python For All'
print(p_for_all.replace('All', 'Everyone'))

businesses = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(businesses.split(","))
print(company.split(" "))
print(company[0])
print(company[-1])
print(company[10])
phrase = 'Python For All'
print(''.join(word[0] for word in phrase.split()))
phrase2 = 'Coding For All'
print(''.join(word[0] for word in phrase2.split()))
print(phrase2.index('C'))
print(phrase2.index('F'))
print(phrase2.rindex('l'))
phrase3 = 'You cannot end a sentence with because because because is a conjunction'
print(phrase3.find('because'))
print(phrase3.rfind('because'))
phrase4 = 'You cannot end a sentence with because because because is a conjunction'
start = phrase4.find('because')
end = phrase4.rfind('because') + len('because')
print(phrase4[start: end])
phrase5 =  'You cannot end a sentence with because because because is a conjunction'
start = phrase5.find('because')
end = phrase5.rfind('because') + len('because')
print(phrase5[start : end])
print(company)
print(company.startswith('coding'))
print(company.endswith('coding'))
phrase6 = '   Coding For All      '

print(phrase6.strip())
print('is this and identifier  30DaysOfPython', ('30DaysOfPython').isidentifier())
print('is this and identifier  thirty_days_of_python', ('thirty_days_of_python').isidentifier())
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(libraries))
print('I am enjoing this challend. \nI just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Arman\t20\tUSA\tSeatle')

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, int(area)))

print('{} + {} = {}'.format(8, 6, 8 + 6))
print('{} - {} = {}'.format(8, 6, 8 - 6))
print('{} * {} = {}'.format(8, 6, 8 * 6))
print('{} / {} = {}'.format(8, 6, 8 / 6))
print('{} % {} = {}'.format(8, 6, 8 % 6))
print('{} // {} = {}'.format(8, 6, 8 // 6))
print('{} ** {} = {}'.format(8, 6, 8 ** 6))
