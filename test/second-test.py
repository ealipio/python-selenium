import unittest
from selenium import webdriver
from config import *


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(CHROME_PATH)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get(URL)
        self.assertIn('Google', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
