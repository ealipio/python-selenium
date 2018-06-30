from selenium import webdriver
from config import *

browser = webdriver.Chrome(CHROME_PATH)
browser.get(URL)
browser.title
elem = browser.find_element_by_id('lst-ib')
elem.send_keys('I will capture this')
print(browser.get_window_size())
browser.save_screenshot("screen.png")
browser.quit()
