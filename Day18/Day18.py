import re
from collections import Counter
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph)
word_count = Counter(words)
result = [(count, word) for word, count in word_count.items()]
result = sorted(result, reverse=True)

print(result)

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

numbers = re.findall(r'-?\d+', text)
print(numbers)

numbers = [int(n) for n in numbers]

distance = max(numbers) - min(numbers)
print(distance)

def valid(string):
    validation = re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', string)
    return bool(validation)
print(valid('stringwith'))

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(i:str):
    return re.sub(r'[@%&$;#]', '', i)
print(clean_text(sentence))
new_sentence = clean_text(sentence)
count = Counter(re.split(" ", new_sentence))

result = [(c, word) for word, c in count.items()]
print(sorted(result, reverse=True))
