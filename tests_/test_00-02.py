from pages_.mainPage import MainPage
from tests_.baseTest import BaseTestWithoutLogIn


class CookieClicker(BaseTestWithoutLogIn):

    def test_one_click_to_cookie(self):
        mainPageObj = MainPage(self.driver)
        mainPageObj.click_to_language_dropdown()
        mainPageObj.click_to_cookie_button_in_a_loop()

        # assertion part is missing
