from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class DeletePersons(BasePage):
    # selectors

    ADD_BUTTON = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[5]'
    PERSON = '//*[text()="Person"]'
    FIRST_NAME = '//div[2]/div[1]/div/div/input'
    LAST_NAME = '//div[2]/div[2]/div/div/input'
    SAVE_BUTTON = '//span[text()="Save"]'
    CONFIRMATION_ASSERT = '//*[text()=" was added successfully!"]'
    FINISH = '//*[@id="root"]//button/span[1]'
    PEOPLE = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[3]/div[2]/span'
    CHECK_BOX = '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/label/span[1]/span[1]/input'
    BUTTON_DELETE = '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[3]/div[1]/div/button/span[1]/div'
    DELETE = '/html/body/div[3]/div[3]/div/div[3]/button[2]'
    CONFIRMATION_DELETE = '//*[@id="client-snackbar"]/div/div/span'
    GO_HOUSEHOLD = '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]'


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

    def finish(self):
        self.driver.find_element(By.XPATH, self.FINISH).click()
        sleep(2)

    def click_people(self):
        self.wait_for_elem(self.PEOPLE)
        self.driver.find_element(By.XPATH, self.PEOPLE).click()
        expected = 'https://jules.app/people'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, "You are not on the People page")

    def click_select_all(self):
        self.wait_for_elem(self.CHECK_BOX)
        self.driver.find_element(By.XPATH, self.CHECK_BOX).click()

    def delete_persons(self):
        self.wait_for_elem(self.BUTTON_DELETE)
        self.driver.find_element(By.XPATH, self.BUTTON_DELETE).click()

    def click_delete(self):
        self.wait_for_elem(self.DELETE)
        self.driver.find_element(By.XPATH, self.DELETE).click()
        sleep(2)

    def delete_confirmation(self):
        self.wait_for_elem(self.CONFIRMATION_DELETE)
        self.driver.find_element(By.XPATH, self.CONFIRMATION_DELETE).is_displayed()
        self.driver.find_element(By.XPATH, self.GO_HOUSEHOLD).click()
