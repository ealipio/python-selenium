from config import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RedmineLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_PATH)

    def test_login(self):
        driver = self.driver
        driver.get(URL_REDMINE)
        # Login into the application
        elem = driver.find_element_by_id('username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('password')
        elem.send_keys(PWD, Keys.RETURN)
        logged = driver.find_element_by_css_selector('div#loggedas')
        assert "Logged in as eisson" in logged.text

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
