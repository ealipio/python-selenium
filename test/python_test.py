import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonSearch(unittest.TestCase):
    url = 'http://www.python.org'
    wait_time = 5
    chrome_path = 'C:\eisson\python\myenv\drivers\chromedriver.exe'
    gecko_path = 'C:\eisson\python\myenv\drivers\geckodriver.exe'
    ie_path = 'C:\eisson\python\myenv\drivers\MicrosoftWebDriver.exe'

    # The setUp is part of initialization, this method will get called before every test function which you are going to write in this test case class. Here you are creating the instance of Chrome WebDriver.
    def setUp(self):
        self.driver = webdriver.Chrome(self.chrome_path)
    # This is the test case method. The test case method should always start with characters test. The first line inside this method create a local reference to the driver object created in setUp method.
    def test_search(self):
        driver = self.driver
        driver.get(self.url)
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert 'No results found.' not in driver.page_source
    
    # The tearDown method will get called after every test method. This is a place to do all cleanup actions. In the current method, the browser window is closed. You can also call quit method instead of close. The quit will exit the entire browser, whereas close will close a tab, but if it is the only tab opened, by default most browser will exit entirely.:    
    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()