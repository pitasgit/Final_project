from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from pages.base_page import BasePage
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains


class HouseholdPage(BasePage):
    # selectors

    LOGIN_BUTTON = '//button[@id="login"]'
    ADD_BUTTON = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[5]'
    PERSON = '//*[text()="Person"]'
    FIRST_NAME = '//div[2]/div[1]/div/div/input'
    LAST_NAME = '//div[2]/div[2]/div/div/input'
    SAVE_BUTTON = '//span[text()="Save"]'
    COOKIES = (By.XPATH, '//button[@id="onesignal-slidedown-cancel-button"]')
    CONFIRMATION_ASSERT = '//*[text()=" was added successfully!"]'
    FINISH = '//*[@id="root"]//button/span[1]'

    # folosim PAGE OBJECT MODEL pentru ca putem reutiliza codul in cazul in care ceva se schimba
    # actions
    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def click_add_button(self):
        self.wait_for_elem(self.ADD_BUTTON)
        self.driver.find_element(By.XPATH, self.ADD_BUTTON).click()

    def add_person(self):
        self.wait_for_elem(self.PERSON)
        self.driver.find_element(By.XPATH, self.PERSON).click()

    def first_name_input(self, first_name):
        self.wait_for_elem(self.FIRST_NAME)
        self.driver.find_element(By.XPATH, self.FIRST_NAME).send_keys(first_name)

    def last_name_input(self, last_name):
        self.wait_for_elem(self.LAST_NAME)
        self.driver.find_element(By.XPATH, self.LAST_NAME).send_keys(last_name)

    def save_button(self):
        self.wait_for_elem(self.SAVE_BUTTON)
        self.driver.find_element(By.XPATH, self.SAVE_BUTTON).click()
        sleep(5)

    def validate_addition(self):
        sleep(1)
        self.wait_for_elem(self.CONFIRMATION_ASSERT)
        expected = 'Silviu Petre was added successfully!'
        actual = self.driver.find_element(By.XPATH, self.CONFIRMATION_ASSERT).text
        self.assertEqual(expected, actual, "The person was not added")

    def push_notification(self):
        self.driver.find_element(*self.COOKIES).click()

    def finish(self):
        self.driver.find_element(By.XPATH, self.FINISH).click()
        sleep(5)
