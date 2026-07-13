import requests

url = 'https://api.thecatapi.com/v1/breeds' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
cats = response.json()
print(type(cats))
print(cats[:1])

weights = []
for cat in cats:
    weight = cat['weight']['metric']
    low, high = weight.split(' - ')

    low = float(low)
    high = float(high)
    
    avg = (low + high) / 2
    weights.append(avg)

print(weights)

import statistics
print(min(weights))
print(max(weights))
print(statistics.mean(weights))
print(statistics.median(weights))
print(statistics.stdev(weights))


lives = []
for cat in cats:
    life = cat['life_span']
    low, high = life.split(' - ')

    low = float(low)
    high = float(high)
    
    avg = (low + high) / 2
    lives.append(avg)

print(lives)

import statistics
print(min(lives))
print(max(lives))
print(statistics.mean(lives))
print(statistics.median(lives))
print(statistics.stdev(lives))


from collections import Counter

countries = []
breed = []
for cat in cats:
    countries.append(cat['origin'])
    breed.append(cat['name'])

country_count = Counter(countries)
breed_count = Counter(breed)


print(country_count)
print(breed_count)


