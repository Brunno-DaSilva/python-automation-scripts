###########################################
#           Automate web browsing
###########################################
# 1.  import Selenium 
from selenium import webdriver
# 2. call Chrome driver and pass the path location
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
# 3.  pass the URL to be opened
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
