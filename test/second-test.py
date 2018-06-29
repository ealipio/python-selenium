import unittest
from selenium import webdriver


class GoogleTestCase(unittest.TestCase):
    chrome_path = 'C:\eisson\python\myenv\drivers\chromedriver.exe'
    url = 'http://www.google.com'

    def setUp(self):
        self.browser = webdriver.Chrome(self.chrome_path)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get(self.url)
        self.assertIn('Google', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
