from pages.home_page import HomePage
from tests.test_data import TestData

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        # Stworzyć instancję klasy HomePage
        # Aby uzyskać dostęp do mechanizmów tej strony
        self.home_page = HomePage(self.driver)
        self.test_data = TestData()

    def tearDown(self):
        self.driver.quit()
