import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
file = open('converse.csv', 'w',  encoding='utf-8_sig',  newline='\n')
f_obj = csv.writer(file)
f_obj.writerow(['Model', 'Price', 'Image'])
page = 1
while page < 6:
    url = f'https://www.ebay.com/sch/15709/i.html?_from=R40&_nkw=%28Converse+Chuck+Taylor%2C+Converse+All+Star%2C+Converse+Canvas%29&LH_TitleDesc=0&LH_BIN=1&LH_ItemCondition=1000&_pgn=' + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sub_soup = soup.find('div', class_='srp-river-results clearfix')
    all_converse = sub_soup.find_all('li', class_="s-item")
    for each in all_converse:
        img_url = each.img.get('src')
        model = each.h3.text
        price = each.find('span', class_='s-item__price').text
        f_obj.writerow([model, price, img_url])
    page += 1
    sleep(randint(15, 20))

