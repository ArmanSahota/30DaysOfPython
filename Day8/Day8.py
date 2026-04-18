dog = {}
dog['name'] = 'Pugg3r'
dog['breed'] = 'Pug'
dog['color'] = 'Black and White'
dog['legs'] = 4
dog['age'] = 67

student = {}
student['First Name'] = 'Arman'
student['Last Name'] = 'Singh'
student['Gender'] = 'Male'
student['Age'] = 69
student['Marital status'] = False
student['Skills'] = ['Python', 'SQL', 'Strong', 'AWS']
student['Country'] = 'USA'
student['City'] = 'Seattle'
student['Address'] = '763 31st ave S'

print(f'student dictionary is {len(student)} keys long')
print(f"The student\'s skills are {student['Skills']} and the skills tab is a {type(student['Skills'])}")
student['Skills'].extend(['Git', 'Bash'])
print(f'The student\'s skills are {student['Skills']}')
print(list(student.keys()))
print(list(student.values()))

students = tuple(student.items())

print(student.pop('Marital status'))

del student


