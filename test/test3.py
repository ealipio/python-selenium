import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import *
'''
Using facebook 
'''

user = 'YOUR_EMAIL_DUH!'
pwd = 'YOUR_PASSWORD'
url = 'http://www.facebook.com'
wait_time = 5
gecko_path = 'C:\eisson\python\myenv\drivers\geckodriver.exe'
ie_path = 'C:\eisson\python\myenv\drivers\MicrosoftWebDriver.exe'

driver_path = CHROME_PATH

browser = webdriver.Chrome(driver_path)
browser.get(url)

elem = browser.find_element_by_id('email')
elem.send_keys(user)
elem = browser.find_element_by_id('pass')
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(wait_time)
browser.close()
