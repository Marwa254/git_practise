from statistics import mean

import requests
from bs4 import BeautifulSoup

#clearly define the base url and add extensions from there by concactinating them to the base url
BASE_URL = "https://books.toscrape.com"

#more complex url formed by joining base and the extension
url = BASE_URL + "/catalogue/category/books/business_35/index.html"

#now I send a request and save as response
response = requests.get(url)

#Convert the response in BeautifulSoup format and save as soup object
soup = BeautifulSoup(response.text, "lxml")

#get the price tags
price_tags = soup.find_all("p", {"class": "price_color"})

#list out the prices and if are floats, declare them, then print
prices = [float(price.text[2:])for price in price_tags] 
print(prices)
print(mean(prices))

