from selenium import webdriver
from selenium.webdriver.common.by import By
from trial_page import TrialPage

browser = webdriver.Chrome()

class TrainingGroundPage:
	def __init__(self, driver):
		self.driver = driver
		self.url = 'https://techstepacademy.com/training-ground'

	def go(self):
		self.driver.get(self.url)

	def type_into_input(self, text):
		inpt = self.driver.find_element(By.ID, 'ipt1')
		inpt.clear()
		inpt.send_keys(text)
		return None

	def get_input_text(self):
		inpt = self.driver.find_element(By.ID, 'ipt1')
		# breakpoint()
		elem_text = inpt.get_attribute('value')
		return elem_text

	def click_button_1(self):
		button = self.driver.find_element(By.ID)
		button.click()
		return None



test_value = 'it worked'

# Test
trial_page = TrialPage(driver=browser)
trial_page.stone_input.input_text("It Worked!")
trial_page.stone_button.click()

input()

# Training Grounds
training_page = TrainingGroundPage(driver=browser)
training_page.go()
training_page.type_into_input(test_value)
txt_from_input = training_page.get_input_text()
assert txt_from_input == test_value, f"Test Failed: Input did not match expected {test_value}."
print("Test Passed.")