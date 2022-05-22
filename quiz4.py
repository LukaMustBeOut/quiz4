import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv


file = open('products.csv', 'w', newline='\n')
pro_file = csv.writer(file)
pro_file.writerow(['image', 'category', 'price'])

page = 1
while page < 6:
    resp = requests.get(f'https://www.ecrater.com/c/66/computers-networking?&srn={page}')
    # print(resp.status_code)
    # print(resp.url)
    soup = BeautifulSoup(resp.text, "html.parser")
    items = soup.find('ul', id="product-list-grid")

    each = items.find_all('li', class_='product-item')
    for i in each:
        price = i.div.span.text
        # print(price)
        product_image = i.a.img.get('src')
        # print(product_image)
        description = i.a.img.get('title')
        product_category = i.find('a', class_='product-category').text
        # print(product_category)

        pro_file.writerow([product_image, product_category, price])

    sleep(randint(15, 20))
    page += 1
