from selenium import webdriver

chrome_path = 'C:\eisson\python\myenv\drivers\chromedriver.exe'
url = 'https://www.google.com/'

browser = webdriver.Chrome(chrome_path)
browser.get(url)
browser.title
elem = browser.find_element_by_id('lst-ib')
elem.send_keys('I will capture this')
browser.save_screenshot("screen.png")
browser.quit()
