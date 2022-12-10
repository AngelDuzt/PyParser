import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://parsesite.ru/ru/upcoming'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

HOST = 'https://'

FILE = 'sites.csv'

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params=params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('li', class_ = 'last')
    a = str(pagination[-1])
    c = ""
    for i in a:
        if i.isdigit():
            c += i
    return int(c)

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_= 'item')
    sites = []
    for item in items:
       a = item.find('a')['href']
       a = a.rpartition('/')[-1]
       sites.append({
           'link': HOST + a
        })
    return sites

def save_file(items, path):
    with open(path, 'w', newline = '') as file:
        writer = csv.writer(file, delimiter = ',')
        for item in items:
            writer.writerow([item['link']])

def main():
    html = get_html(URL)
    if html.status_code == 200:
        sites = []
        pages_count = get_pages_count(html.text)
        pages_count = 2500
        for page in range (1, pages_count+1):
            print(f'Парсинг страницы {page} из {pages_count}')
            html = get_html(URL, params={'page': page})
            sites.extend(get_content(html.text))
        save_file(sites, FILE)
        print(f'Получено {len(sites)} проверенных сайтов')
    else:
        print('Error')
if __name__ == '__main__':
    main()
