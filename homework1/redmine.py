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
# browser.set_page_load_timeout(60)
# verify if user is logged
logged = browser.find_element_by_css_selector('div#loggedas')
assert "Logged in as eisson" in logged.text
browser.quit()  # close the browser