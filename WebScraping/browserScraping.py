
###########################################
#          Simple Browser Scrapping 
###########################################

# # 1. import libraries 
# import requests
# # 4A. Parse the HTML document
# from bs4 import BeautifulSoup

# # 2. Get website url assign it to a variable 
# url = 'http://quotes.toscrape.com/'

# # 3. Connecting URL and getting the response
# response = requests.get(url)

# # 4B. Parse the HTML document
# soup = BeautifulSoup(response.text, 'lxml'); 

# # 5. Print it to verify if our parse worked correctly
# print(soup)


###########################################
#     Isolating Data from browser 
###########################################


# 1. import libraries 
import requests
# 4A. Parse the HTML document
from bs4 import BeautifulSoup

# 2. Get website url assign it to a variable 
url = 'http://quotes.toscrape.com/'

# 3. Connecting URL and getting the response
response = requests.get(url)

# 4B. Parse the HTML document
soup = BeautifulSoup(response.text, 'lxml'); 

# 5. Inspect the website and locate what html tags and class 
#    are holding the data you want to isolate

# get all quotes
quotes = soup.find_all('span', class_='text')

# get all authors 
authors = soup.find_all('small', class_='author')
# get all tags 
tags = soup.find_all('div', class_='tags')

# 6. loop through each quote
# for quote in quotes: 
#     print(quote.text); 

# Altering the for loop since there is one author to a quote 
for i in range(0, len(quotes)):
    print("Quotes: " + quotes[i].text)
    print("Author: " + authors[i].text)
    quoteTags = tags[i].find_all('a', class_="tag")
    for quoteTag in quoteTags: 
        print( "Tags: "+ quoteTag.text)
    print("--------------------------------------------")

