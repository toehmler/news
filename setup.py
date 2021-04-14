import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import favicon
from PIL import Image
from io import BytesIO


filepath = 'server/sources.csv'
url = 'https://www.adfontesmedia.com/rankings-by-individual-news-source/'

def format_url(url):
    idx = url.find('/')
    new_url = url[:idx+2] + 'www.' + url[idx+2:]
    return new_url

def parse_source(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    title = soup.find("h1").get_text()[:-21]
    container = soup.find('article')
    link = container.find('a')['href']
    ratings = container.find_all('h2')[1].find_next_siblings('p')[3:5]
    reliability = ratings[0].get_text()[13:]
    bias = ratings[1].get_text()[6:]
    try:
        icons = favicon.get(link)
    except:
        link = format_url(link)
        try:
            icons = favicon.get(link)
        except:
            icons = ['']
    return ([title, link, reliability, bias], icons)

# look through the list of icons to try to find the largest, most square
def select_icon(icons):
    selected = ('',-1,-2)
    for icon in icons:
        resp = requests.get(icon.url)
        try:
            img = Image.open(BytesIO(resp.content))
        except:
            continue
#        img = Image.open(BytesIO(requests.get(icon.url, stream=True).raw))
        current = (icon.url, img.size[0], img.size[1])
        if selected[1] != selected[2] and current[1] == current[2]:
            selected = current
        elif selected[1] == selected[2] and current[1] == current[2]:
            if current[1] > selected[2]:
                selected = current
        elif selected[1] != selected[2] and current[1] != current[2]:
            if current[1] * current[2] > selected[1] * selected[2]:
                selected = current
    return selected[0]

if __name__ == "__main__":

    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    sources = soup.find_all('article')

    out_file = open(filepath, 'w', newline='')
    writer = csv.writer(out_file)

    for i in tqdm(range(len(sources))):
        source = sources[i]
        link = source.find("a")['href']
        source_data = parse_source(link)
        if len(source_data[1]) > 1:
            icon = select_icon(source_data[1])
        else:
            icon = source_data[0][0]
        source_data[0].append(icon)
        writer.writerow(source_data[0])

    out_file.close()

