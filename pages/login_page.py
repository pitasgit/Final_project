from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class LoginPage(BasePage):
    # selectors

    USER_INPUT = '//div[1]/div/div/input'
    PASS_INPUT = '//div[2]/div/div/input'
    LOGIN_BUTTON = '//div/div[3]/button/span[1]'
    INVALID_CREDENTIALS_ERROR = '//*[@id="client-snackbar"]/div/span'
    VALID_LOGIN = '//*[@id="root"]/div[1]/div[1]/div/div[1]/span/span'
    COOKIES = '//*[@id="onesignal-slidedown-cancel-button"]'

    # actions

    def user_input(self, user):
        self.wait_for_elem(self.USER_INPUT)
        self.driver.find_element(By.XPATH, self.USER_INPUT).send_keys(user)

    def pass_input(self, pasw):
        self.wait_for_elem(self.PASS_INPUT)
        self.driver.find_element(By.XPATH, self.PASS_INPUT).send_keys(pasw)

    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
        self.driver.maximize_window()

    def validate_invalid_credentials_error(self):
        sleep(1)
        self.wait_for_elem(self.INVALID_CREDENTIALS_ERROR)
        expected = 'Invalid email/password combination'
        actual = self.driver.find_element(By.XPATH, self.INVALID_CREDENTIALS_ERROR).text
        self.assertEqual(expected, actual, "Invalid username/password")

    # def validate_login(self):
    #     self.wait_for_elem(self.VALID_LOGIN)
    #     expected = 'https://jules.app/search/all'
    #     actual = self.driver.current_url
    #     self.assertEqual(expected, actual, "You are not on the household page")

    def logged_in(self):
        self.wait_for_elem(self.VALID_LOGIN)
        expected = 'https://jules.app/search/all'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, "You are not on the household page")
    def cookies(self):
        self.wait_for_elem(self.COOKIES)
        self.driver.find_element(By.XPATH, self.COOKIES).click()