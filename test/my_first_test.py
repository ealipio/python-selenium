from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_PATH = 'C:\eisson\python\myenv\drivers\chromedriver.exe'
URL = 'https://www.google.com/'

BROWSER = webdriver.Chrome(CHROME_PATH)
BROWSER.get(URL)
ELEM = BROWSER.find_element_by_id('lst-ib')  # this is the input search box ID
ELEM.send_keys('do a barrel roll' + Keys.RETURN)
BROWSER.quit()  # close the browser
# Xpath=//tagname[@attribute='value']
# driver.find_element_by_xpath(“//span[@id=’firstname-placeholder’]”)
# driver.find_element_by_css_selector(“input#FirstName”)

# locator = '//input[@id="Name"]'
# first_name_we = driver.find_element(By.XPATH, locator)
# first_name_we.clear()
# first_name_we.send_keys(“Cristian”)

# learn_more_link_we = driver.find_element(By.PARTIAL_LINK_TEXT, ‘Learn more’)
# learn_more_link_we.click()

# option_we = driver.find_element(By.ID, ‘keep_me_logged_in’)
# if option_we.is_selected():
#     print(“Checkbox is toggled On”)
# else:
#     print(“Checkbox is toggled Off”)

# Radio button
# def select_rb(option):
#     options_we = driver.find_elements(locator)

#     for o in options_we:
#         if o.text == option:
#             o.click()

# Select Option
# from selenium.webdriver.support.select import Select
# drop_down_we = driver.find_element_by_name(‘education’)
# drop_down = Select(web_element)

# drop_down.select_by_index(2)
# drop_down.select_by_value(‘graduate’)
# drop_down.select_by_visible_text(‘Graduate’)