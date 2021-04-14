import csv
import favicon
import requests
from PIL import Image
from io import BytesIO
from tqdm import tqdm

def format_url(url):
    idx = url.find('/')
    new_url = f'{url[:idx+2]}www.{url[idx+2:]}'
    return new_url

def resolve_icons(url):
    try:
        icons = favicon.get(url)
    except:
        url = format_url(url)
        try:
            icons = favicon.get(url)
        except:
            icons = ['']

    return (url, icons)

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

def get_icon_fname(base_url, icon_url):
    start = base_url.find('/')
    if base_url[start+2:start+6] == 'www.':
        start += 6
    else:
        start += 2
    end = base_url.rfind('.')
    icon_url = icon_url[icon_url.rfind('/')+1:]
    return f'{base_url[start:end]}_{icon_url}'

def save_icon(base_url, icon_url):
    # downloads the icon at a given url and saves it in the icon folder
    # returns a string representing the local path to the icon
    filename = get_icon_fname(base_url, icon_url)
    out_path = f'./client/public/source_icons/{filename}'
    response = requests.get(icon_url)
    out_file = open(out_path, 'wb')
    out_file.write(response.content)
    out_file.close()
    return out_path

if __name__ == "__main__":

    # load csv files for reading / writing
    in_fname = 'server/output.csv'
    out_fname = 'server/output_fixed.csv'
    in_file = open(in_fname)
    out_file = open(out_fname, 'a', newline='')
    reader = csv.reader(in_file)
    writer = csv.writer(out_file)

    count = 0
    for row in reader:
        if count > 239:
            print(count)
            # resolve icons, select the best one and download
            url, icons = resolve_icons(row[1])
            if icons != [''] and icons != []:
                icon_url = select_icon(icons)
                if len(icon_url) > 0:
                    icon_path = save_icon(url, icon_url)
                else:
                    icon_path = ''
            else:
                icon_path = ''
            new_row = [row[0], url, row[2], row[3], icon_path]
            writer.writerow(new_row)
        count += 1
    in_file.close()
    out_file.close()

'''
97
126
229
230?
240
'''




