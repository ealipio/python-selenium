from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./drivers/chromedriver.exe")
browser.get('https://www.google.com/')
browser.title
elem = browser.find_element_by_id('lst-ib')  # this is the input search box ID
elem.send_keys('do a barrel roll' + Keys.RETURN)
# elem.send_keys('#google gravity')

browser.quit()  # close the browser
