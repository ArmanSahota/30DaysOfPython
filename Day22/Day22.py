import requests
from bs4 import BeautifulSoup
#url = "https://www.bu.edu/president/boston-university-facts-stats/"

#response = requests.get(url)
#content = response.content # we get all the content from the website
#soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
#print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
#print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
#print(soup.body) # gives the whole page on the website
#print(response.status_code)
#print(type(soup.body))

#import json
#data = {'title': soup.title.get_text(strip=True),
 #       'content' : soup.body.get_text(separator="\n", strip=True)}
#
#with open('./Day22/data.json', 'w', encoding='utf-8') as f:
#    json.dump(data, f, indent= 4)


import json
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find_all("table")[0]

data = []

for row in table.find_all("tr")[1:]:
    cols = row.find_all(["th", "td"])

    if cols:
        data.append([col.get_text(strip=True) for col in cols])

with open("president.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)