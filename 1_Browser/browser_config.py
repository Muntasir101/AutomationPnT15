from selenium import webdriver
import unittest


class Browser_Basic(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_browser_launch(self):
        # Browser launch
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com")


if __name__ == '__main__':
    unittest.main()
