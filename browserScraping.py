
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

# 5. Print it to verify if our parse worked correctly
print(soup)
