###Write a function which count number of lines and number of words in a text. All the files are in the data the folder:

#Read obama_speech.txt file and count number of lines and words
#Read michelle_obama_speech.txt file and count number of lines and words
##Read donald_speech.txt file and count number of lines and words
#Read melina_trump_speech.txt file and count number of lines and words

def length(filename:str):
    f = open(f"./data/{filename}")
    return len(f.readline())
print(length('obama_speech.txt'))
print(length('michelle_obama_speech.txt'))
print(length('donald_speech.txt'))
print(length('melina_trump_speech.txt'))

import json
from collections import Counter

def most_spoken_languages(filename:str, number:int):
    with open(f'./data/{filename}', 'r', encoding= 'utf-8') as f:
        countries = json.load(f)
    languages = []
    for country in countries:
        languages.extend(country['languages'])
    count = Counter(languages)
    max_freq = max(count.values())

    freq = [[] for _ in range(max_freq + 1)]
    for language, num, in count.items():
        freq[num].append(language)
    results = []
    for i in range(len(freq)-1, -1, -1):
        for language in freq[i]:
            results.append((language, i))
            number -= 1
            if number == 0:
                return results
            
print('Theres are the top 2 languages spoken:', most_spoken_languages('countries_data.json', 2))

def most_populated_countries(filename:str, number:int):
    with open(f'./data/{filename}', 'r', encoding= 'utf-8') as f:
        countries = json.load(f)
    population = []
    for country in countries:
        population.append({'country':country['name'], 'population':country['population']})
    population.sort(key=lambda x: x['population'], reverse=True)

    return population[:number]
            
print(f'Theres are the top 5 populated Countries:', most_populated_countries('countries_data.json', 5))

import re
f = open('./data/email_exchanges_big.txt', 'r', encoding="utf-8")
text = f.read()
result = []
result.extend(re.findall(r'[\w.-]+@[\w.-]+\.\w+', text))
print(len(result))
text = f.close()

def find_most_common_words(filename:str, number:int):
    with open(f'./data/{filename}', 'r', encoding='utf-8') as f:
        text = f.read()
    count = Counter(re.findall(r'\b\w+\b', text))
    max_freq = max(count.values())
    freq = [[] for _ in range(max_freq + 1)]
    for word, c in count.items():
        freq[c].append(word)
    result = []
    for i in range(len(freq) -1, -1, -1):
        for j in freq[i]:
            result.append((i, j))
            number -= 1
            if number == 0:
                return result
    
print(find_most_common_words('romeo_and_juliet.txt', 10))

print("most comon word in the obama speech", find_most_common_words('obama_speech.txt', 5))

print("most comon word in the trump speech", find_most_common_words('donald_speech.txt', 5))

print("most comon word in the michelle obama speech", find_most_common_words('michelle_obama_speech.txt', 5))

print("most comon word in the miliania speech", find_most_common_words('melina_trump_speech.txt', 5))

def similarity(file1:str, file2:str):

    def clean_text(filename:str):
        with open(f'./data/{filename}') as f:
            text = f.read().lower()
        return re.findall(r'\b\w+\b', text)
    
    def remove_support_words(ls:list):
        import sys
        sys.path.append(r'd:\30DaysOfPython\data')
        from stop_words import stop_words
        result = []
        for word in ls:
            if word not in stop_words:
                result.append(word)
        return result
    clean1 = clean_text(file1)
    clean2 = clean_text(file2)

    rsw1 = remove_support_words(clean1)
    rsw2 = remove_support_words(clean2)

    common = 0
    for word in rsw1:
        for word in rsw2:
            common += 1
    similarity = (common / len(rsw1)) * 100

    return similarity

print(similarity('michelle_obama_speech.txt', 'melina_trump_speech.txt'))

with open('./data/hacker_news.csv', 'r', encoding='utf-8') as f:
    text = f.readlines()
Pcount = 0
jscount = 0
javacount = 0
for i in text:
    if re.findall(r'python', i, re.IGNORECASE):
        Pcount += 1
    if re.findall(r'javascript', i, re.IGNORECASE):
        jscount += 1
    if re.findall(r'\bjava\b', i, re.IGNORECASE):
        javacount += 1



    
print(Pcount)
print(jscount)
print(javacount)
        
             



