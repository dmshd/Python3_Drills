from selenium.webdriver.common.by import By
from base_element import BaseElement
from base_page import BasePage
from locator import Locator

class TrialPage(BasePage):

    url = 'https://techstepacademy.com/training-ground'

    @property
    def stone_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r1Input')
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def stone_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r1Btn')
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def secret_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="r2Input"]')
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def secret_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r2Btn')
        return BaseElement(
            self.driver,
            locator=locator
        )

