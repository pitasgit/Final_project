from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class ConnectionPage(BasePage):
    # selectors

    ADD_BUTTON = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[5]'
    ADD_CONNECTION = '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div/div/a[5]/div'
    CREATE_CONNECTION = '//*[@id="root"]/div[1]/div[3]/div/div[4]/div[3]/div[2]/div/div/div[2]'
    INSERT_CONNECTION_NAME = '//*[@id="root"]/div[1]/div[3]/div/div[4]/div[3]/div[2]/div/form/div[1]/div[2]/div/input'
    SAVE_BUTTON = '//*[@id="root"]/div[1]/div[3]/div/div[4]/div[3]/div[2]/div/form/div[2]/div/button/span'
    CONFIRMATION_ASSERT = '//*[text()="Your Connection was added successfully!"]'
    FINISH = '//*[@id="root"]/div[1]/div[3]/div/div[4]/div[3]/div[2]/div/div/div[2]/button[3]'
    SELECT_CONNECTION = '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[3]/div[1]/div[3]/div/button[1]'
    SEARCH_BUTTON = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/span'
    CONNECTION_BUTTON = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[4]'
    VIEW_MORE = '//*[@id="menu-list-grow"]/div[2]/li/span[1]'
    CONFIRM_DELETE_CONNECTION = '/html/body/div[3]/div[3]/div/div[3]/button[2]/span[1]'
    CLOSE_EDIT = '/html/body/div[3]/div[3]/div/div[3]/button[2]'

    # actions

    def click_add_button(self):
        self.wait_for_elem(self.ADD_BUTTON)
        self.driver.find_element(By.XPATH, self.ADD_BUTTON).click()

    def add_connection(self):
        self.wait_for_elem(self.ADD_CONNECTION)
        self.driver.find_element(By.XPATH, self.ADD_CONNECTION).click()

    def create_connection(self):
        self.wait_for_elem(self.CREATE_CONNECTION)
        self.driver.find_element(By.XPATH, self.CREATE_CONNECTION).click()

    def insert_connection_name(self):
        self.wait_for_elem(self.INSERT_CONNECTION_NAME)
        self.driver.find_element(By.XPATH, self.INSERT_CONNECTION_NAME).send_keys('user')

    def save_button(self):
        self.wait_for_elem(self.SAVE_BUTTON)
        self.driver.find_element(By.XPATH, self.SAVE_BUTTON).click()
        sleep(5)

    def validate_addition(self):
        sleep(1)
        self.wait_for_elem(self.CONFIRMATION_ASSERT)
        expected = 'Your Connection was added successfully!'
        actual = self.driver.find_element(By.XPATH, self.CONFIRMATION_ASSERT).text
        self.assertEqual(expected, actual, "The connection was not added")

    def click_connection_button(self):
        self.wait_for_elem(self.CONNECTION_BUTTON)
        self.driver.find_element(By.XPATH, self.CONNECTION_BUTTON).click()

    def select_connection(self):
        self.wait_for_elem(self.SELECT_CONNECTION)
        self.driver.find_element(By.XPATH, self.SELECT_CONNECTION).click()

    def delete_user_connection(self):
        self.wait_for_elem(self.VIEW_MORE)
        self.driver.find_element(By.XPATH, self.VIEW_MORE).click()
        self.driver.find_element(By.XPATH, self.CONFIRM_DELETE_CONNECTION)
        self.wait_for_elem(self.CLOSE_EDIT)
        self.driver.find_element(By.XPATH, self.CLOSE_EDIT).click()

    def search_button(self):
        self.wait_for_elem(self.SEARCH_BUTTON)
        self.driver.find_element(By.XPATH, self.SEARCH_BUTTON).click()

    def finish(self):
        self.driver.find_element(By.XPATH, self.FINISH).click()
        sleep(5)
