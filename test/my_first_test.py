from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_PATH = 'C:\eisson\python\myenv\drivers\chromedriver.exe'
URL = 'https://www.google.com/'

BROWSER = webdriver.Chrome(CHROME_PATH)
BROWSER.get(URL)
ELEM = BROWSER.find_element_by_id('lst-ib')  # this is the input search box ID
ELEM.send_keys('do a barrel roll' + Keys.RETURN)

BROWSER.quit()  # close the browser
