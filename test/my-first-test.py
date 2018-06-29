from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_path = 'C:\eisson\python\myenv\drivers\chromedriver.exe'
url = 'https://www.google.com/'

browser = webdriver.Chrome(chrome_path)
browser.get(url)
browser.title
elem = browser.find_element_by_id('lst-ib')  # this is the input search box ID
elem.send_keys('do a barrel roll' + Keys.RETURN)
# elem.send_keys('#google gravity')

browser.quit()  # close the browser
