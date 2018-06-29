import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
Using facebook 
'''

user = "YOUR_EMAIL_DUH!"
pwd = "YOUR_PASSWORD"

browser = webdriver.Chrome("./drivers/chromedriver.exe")
browser.get("http://www.facebook.com")

elem = browser.find_element_by_id("email")
elem.send_keys(user)
elem = browser.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
# browser.close()