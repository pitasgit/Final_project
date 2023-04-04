from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from time import sleep


class ProfilePage(BasePage):
    PEOPLE_PROFILE = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[3]'
    PETRE_UNGUREANU = '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[3]/div[2]/div/div[2]/div/span'
    ATTACHMENTS = '//*[@id="root"]/div[3]/div[2]/div[3]/div[1]/div/div/div/button[2]/span[1]/div/div[2]/span'
    LINKS = '//*[@id="root"]/div[3]/div[2]/div[3]/div[1]/div/div/div/button[3]/span[1]/div/div[2]/span'
    TAGS = '//*[@id="root"]/div[3]/div[2]/div[3]/div[1]/div/div/div/button[4]/span[1]/div/div[2]/span'
    ADD_TAG = '//*[@id="root"]/div[3]/div[2]/div[3]/div[2]/div/div/div[2]/div/span'
    TAG_CLICK = '//*[@id="root"]/div[3]/div[2]/div[3]/div[2]/div/div/div[2]/div'
    CLOSE = '//*[@id="root"]/div[3]/div[2]/div[1]/div[2]/button'
    SEARCH_BACK = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/span'

    def people_profiles(self):
        self.wait_for_elem(self.PEOPLE_PROFILE)
        self.driver.find_element(By.XPATH, self.PEOPLE_PROFILE).click()
        self.driver.find_element(By.XPATH, self.PETRE_UNGUREANU).click()

    def check_profile(self):
        self.wait_for_elem(self.ATTACHMENTS)
        self.driver.find_element(By.XPATH, self.ATTACHMENTS).click()
        self.driver.find_element(By.XPATH, self.LINKS).click()
        self.driver.find_element(By.XPATH, self.TAGS).click()

    def add_tag(self):
        self.wait_for_elem(self.ADD_TAG)
        self.driver.find_element(By.XPATH, self.ADD_TAG).click()
        self.driver.find_element(By.XPATH, self.TAG_CLICK).click()

    def household_back(self):
        self.wait_for_elem(self.CLOSE)
        self.driver.find_element(By.XPATH, self.CLOSE).click()
        self.wait_for_elem(self.SEARCH_BACK)
        self.driver.find_element(By.XPATH, self.SEARCH_BACK).click()
