from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HouseholdPage(BasePage):
    # selectors

    LOGIN_BUTTON = '//button[@id="login"]'
    VALID_LOGIN = '//*[@id="root"]/div[1]/div[1]/div/div[1]/span/span'
    COOKIES = '//*[@id="onesignal-slidedown-cancel-button"]'

    # folosim PAGE OBJECT MODEL pentru ca putem reutiliza codul in cazul in care ceva se schimba
    # actions

    def household_home(self):
        self.wait_for_elem(self.VALID_LOGIN)
        expected = 'https://jules.app/search/all'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, "You are not on the household page")

    def cookies(self):
        self.wait_for_elem(self.COOKIES)
        self.driver.find_element(By.XPATH, self.COOKIES).click()
