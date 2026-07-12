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
with open('./data/countries_data.json', 'r', encoding= 'utf-8') as f:
    countries = json.load(f)

languages = []
for country in countries:
    languages.extend(country['languages'])

from collections import Counter
count = Counter(languages)

max_freq = max(count.values())

freq = [[] for _ in range(max_freq + 1)]

for language, number in count.items():
    freq[number].append(language)

result = []
k = 0

for i in range(len(freq)-1, -1, -1):
    for language in freq[i]:
        result.append((language, i))
        k += 1
        if k == 10:
            break
    if k == 10:
        break
print("top 10 most spoken languages:")
for lang, freqe in result:
    print(lang, freqe)

#def top10C(filename:str):
#    f = open()