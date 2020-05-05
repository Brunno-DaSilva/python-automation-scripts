# 1. import libraries 
import requests
# 4A. Parse the HTML document
from bs4 import BeautifulSoup

# 2. Get website url assign it to a variable 
url = 'https://scrapingclub.com/exercise/list_basic/'

# 3. Connecting URL and getting the response
response = requests.get(url)

# 4B. Parse the HTML document
soup = BeautifulSoup(response.text, 'lxml'); 

# 5. Get the items from the page
items = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")

# 6. loop through and get the data
count = 1
for i in items: 
    itemName = i.find('h4', class_="card-title").text.strip("\n")
    itemPrice = i.find("h5").text
    print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))


