from selenium import webdriver
from selenium.webdriver.common.keys import Keys

EDGE_PATH = 'C:\eisson\python\myenv\drivers\MicrosoftWebDriver.exe'
URL = 'https://www.google.com/'

BROWSER = webdriver.Edge('C:\eisson\python\myenv\drivers\MicrosoftWebDriver.exe')
BROWSER.get(URL)
BROWSER.quit()  # close the browser
