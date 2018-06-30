from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import *

browser = webdriver.Chrome(CHROME_PATH)
browser.get(URL_REDMINE)
# Login into the application
elem = browser.find_element_by_id('username')
elem.send_keys(USER)
elem = browser.find_element_by_id('password')
elem.send_keys(PWD)
elem.send_keys(Keys.RETURN)

browser.quit()  # close the browser
