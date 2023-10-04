import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import time

names = []
categories = []
description = []
ratings = []
prices = []
stat = []
product_info_list = []


#soup = bs(response.text, 'html.parser')

#books = soup.find_all('h3')
book_num = 0

for page in range(1, 6):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    books = soup.find_all('h3')
    for book in books:
        # get links
        book_link = book.find('a')['href']
        book_response = requests.get('http://books.toscrape.com/catalogue/' + book_link)
        book_soup = bs(book_response.content, 'html.parser')
        
        name = book_soup.find('h1').text
        category = book_soup.find('ul', class_ = 'breadcrumb').find_all('a')[2].text.strip()
        desc = book_soup.find('div', class_="content").find_all('p')[3].text.strip()
        rating = book_soup.find('p', class_ = 'star-rating')['class'][1]
        price = book_soup.find('p', class_='price_color').text.strip()
        status = book_soup.find('p', class_='instock availability').text.strip()

        book_num += 1

        # Append data to lists
        names.append(name)
        categories.append(category)
        description.append(desc)
        ratings.append(rating)
        prices.append(price)
        stat.append(status)
        #product_info_list.append(product_info)

# Create a DataFrame
data = {
    'book_name': names,
    'category': categories,
    'description':description,
    'rating': ratings,
    'price': prices,
    'status': stat,
    #'product_info':product_info_list
}

print(book_num)

df = pd.DataFrame(data)
# Export the DataFrame to a CSV file
df.to_csv('book_data.csv', index=False)
