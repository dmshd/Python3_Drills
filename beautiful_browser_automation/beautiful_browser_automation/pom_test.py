from selenium import webdriver
from selenium.webdriver.common.by import By
from base_element import BaseElement
from base_page import BasePage
from locator import Locator

browser = webdriver.Chrome()

class TrainingGroundPage(BasePage):

    url = 'https://techstepacademy.com/training-ground'

    @property
    def button1(self):
        locator = Locator(by=By.ID, value='b1')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )



test_value = 'it worked'

training_page = TrainingGroundPage(driver=browser)

training_page.go()
breakpoint()
assert training_page.button1.text == 'Button1', f"Test Failed: Input did not match expected {test_value}."
training_page.button1.click()