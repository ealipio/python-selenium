from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import *

BROWSER = webdriver.Chrome(CHROME_PATH)
BROWSER.get(URL)
ELEM = BROWSER.find_element_by_id('lst-ib') # this is the input search box ID
ELEM.send_keys('do a barrel roll' + Keys.RETURN)
BROWSER.quit()  # close the browser
