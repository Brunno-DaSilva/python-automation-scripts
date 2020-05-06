###########################################
#           Automate web browsing
###########################################
# 1.  import Selenium 
from selenium import webdriver
# 2. call Chrome driver and pass the path location
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
# 3.  pass the URL to be opened
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# get the message field xPath
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
# write text to the field 
messageField.send_keys('Ciao Mundo')
#  get the msg btn field xPath
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
# submit the btn
showMessageButton.click()

# Get two input fields and the btn, add values to the input, 
# click the btn

inputFieldOne = driver.find_element_by_xpath('//*[@id="sum1"]')
inputFieldOne.send_keys(10)

inputFieldTwo = driver.find_element_by_xpath('//*[@id="sum2"]')
inputFieldTwo.send_keys(3)

addTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
addTotalButton.click()



