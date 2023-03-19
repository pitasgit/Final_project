from selenium.webdriver.chrome import webdriver

from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import unittest
from selenium import webdriver


class BasePage(Browser, unittest.TestCase):
    def wait_for_elem(self, xpath_selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_selector)))
# cu sleep oprim 3 secunde executia testului. cu Explicity wait, acesta cauta testul in fiecare secunda. pe scurt, creste viteza testelor
