from pages.base_page import BasePage


class HomePage(BasePage):

    # actions
    def navigate_to_home_page(self):
        self.driver.get('https://jules.app/sign-in')
