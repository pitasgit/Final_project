from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.set_page_load_timeout(3)
    driver.maximize_window()
    driver.delete_all_cookies()


def close(self):
    self.driver.quit()
