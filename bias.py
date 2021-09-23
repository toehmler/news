import requests
from bs4 import BeautifulSoup
import csv

#tesitn 

apikey = '7b18eaf6c76644afbb3831bbecdbe722'
baseuri = 'https://newsapi.org/v2/sources?&apiKey=' + apikey

#uri = baseuri + '?country=us?language=en'
#uri = "https://newsapi.org/v2/sources?apiKey=7b18eaf6c76644afbb3831bbecdbe722"
#uri += "&country=us&language=en&category=general"



url = "https://www.adfontesmedia.com/rankings-by-individual-news-source/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
sources = soup.find_all("article")

out_file = open('output.csv', 'w', newline='')
writer = csv.writer(out_file)

count = 0

def get_favicon(html, url):
    """Scrape favicon."""
    if html.find("link", attrs={"rel": "icon"}):
        favicon = html.find("link", attrs={"rel": "icon"}).get('href')
    elif html.find("link", attrs={"rel": "shortcut icon"}):
        favicon = html.find("link", attrs={"rel": "shortcut icon"}).get('href')
    else:
        favicon = f'{url.rstrip("/")}/favicon.ico'
    return favicon


for source in sources:
    link = source.find_all("a")[0]['href']
    source_req = requests.get(link)
    source_soup = BeautifulSoup(source_req.content, 'html.parser')
    source_title = source_soup.find("h1").get_text()[:-21]
    source_container = source_soup.find('article')
    source_link = source_container.find('a')['href']
    ratings = source_container.find_all('h2')[1].find_next_siblings('p')[3:5]
    reliability = ratings[0].get_text()[13:]
    bias = ratings[1].get_text()[6:]

    writer.writerow([source_title, source_link, reliability, bias, icon])

out_file.close()
'''
r = requests.get(uri)
r = r.json()["sources"]
for source in r:
    print(source["id"])
'''








