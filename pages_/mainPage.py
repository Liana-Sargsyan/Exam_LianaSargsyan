from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class MainPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.__cookieButtonLocator = (By.XPATH, "//button[@id='bigCookie']")
        self.__languageDropdownLocator = (By.ID, "langSelect-EN")
        self.__cookieClickCountLocator = (By.ID, "cookies")

    def click_to_cookie_button(self):
        cookieButtonElement = self._find_element(self.__cookieButtonLocator)
        self._click_to_element(cookieButtonElement)

    def click_to_cookie_button_in_a_loop(self):
        cookieButtonElement = self._find_element(self.__cookieButtonLocator)
        clickTimes = 10000
        for i in range(clickTimes):
            self._click_to_element(cookieButtonElement)

    def click_to_language_dropdown(self):
        languageButtonElement = self._find_element(self.__languageDropdownLocator)
        self._click_to_element(languageButtonElement)

    def get_cookie_count(self):
        cookieCountElement = self._find_element(self.__cookieClickCountLocator)
        print(str(self._get_element_text(cookieCountElement)))