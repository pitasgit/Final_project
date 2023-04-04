from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EhrPage(BasePage):
    # selectors
    ADD_BUTTON = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[5]'
    ADD_EHR = '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div/div/a[4]/div'
    PETRE = '//*[@id="root"]/div[1]/div[3]/div/div[4]/div[3]/div[2]/div/form/div[1]/div/div/div/div/button/span[1]/svg'
    CONTINUE_BTN = '//*[@id="root"]/div[1]/div[3]/div/div[4]/div[3]/div[2]/div/form/div[2]/div/button/span'
    P_U = '//*[@id="mui-autocomplete-92936-option-0"]/div'
    BACK = '//*[@id="root"]/div[1]/div[3]/div/div[4]/div[2]/div[1]/span[2]'
    CLOSE = '//*[@id="root"]/div[1]/div[3]/div/div[2]/div[2]/span[1]'

    def click_add_button(self):
        self.wait_for_elem(self.ADD_BUTTON)
        self.driver.find_element(By.XPATH, self.ADD_BUTTON).click()

    def add_ehr(self):
        self.wait_for_elem(self.ADD_EHR)
        self.driver.find_element(By.XPATH, self.ADD_EHR).click()

    def back_button(self):
        self.wait_for_elem(self.BACK)
        self.driver.find_element(By.XPATH, self.BACK).click()

    def back_to_hh(self):
        self.wait_for_elem(self.CLOSE)
        self.driver.find_element(By.XPATH, self.CLOSE).click()
