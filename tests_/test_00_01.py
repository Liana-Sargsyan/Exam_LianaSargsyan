from selenium import webdriver
from pages_.mainPage import MainPage
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CookieClicker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")

    def test_one_click_to_cookie(self):
        mainPageObj = MainPage(self.driver)
        mainPageObj.click_to_cookie_button()
        time.sleep(6)
        # self.assertEqual()

    def tearDown(self):
        self.driver.close()
