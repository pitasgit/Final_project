from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogoutPage(BasePage):
    ACCOUNT_BUTTON = '//*[@id="root"]/div[1]/div[1]/div/div[2]/div[3]'
    FORGOT_PASSWORD = '//*[@id="root"]/div/div[2]/form/div/div[3]/a'
    LOG_OUT = '//*[@id="menu-list-grow"]/div[2]/li/span[1]'
    CONFIRM_LOGOUT = '/html/body/div[3]/div[3]/div/div[3]/button[2]/span[1]'

    def account_button(self):
        self.wait_for_elem(self.ACCOUNT_BUTTON)
        account_button = self.driver.find_element(By.XPATH, self.ACCOUNT_BUTTON)
        account_button.click()

    def log_out(self):
        self.wait_for_elem(self.LOG_OUT)
        self.driver.find_element(By.XPATH, self.LOG_OUT).click()
        self.wait_for_elem(self.CONFIRM_LOGOUT)
        self.driver.find_element(By.XPATH, self.CONFIRM_LOGOUT).click()

    def home_page(self):
        self.wait_for_elem(self.FORGOT_PASSWORD)
        expected = 'https://jules.app/sign-in'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, "You are not on the home page")
