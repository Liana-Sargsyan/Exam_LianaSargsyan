from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class MainPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.__cookieButtonLocator = (By.ID, "bigCookie")

    def click_to_cookie_button(self):
        cookieButtonElement = self._find_element(self.__cookieButtonLocator)
        self._click_to_element(cookieButtonElement)
