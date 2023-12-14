import unittest
from selenium import webdriver
from pages_.mainPage import MainPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from testData_.testData import mainPageUrl


class BaseTestWithoutLogIn(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(mainPageUrl)

    def tearDown(self):
        self.driver.close()
