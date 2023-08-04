import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

input2_css_locator = "input[id='ipt2']"
butn4_xpath_locator = "//button[@id='b4']"

# Assign elements
input1_elem = browser.find_element(By.CSS_SELECTOR, input2_css_locator)
butn4_elem = browser.find_element(By.XPATH, butn4_xpath_locator)

# Manipulate elements
input1_elem.send_keys("Test text")
butn4_elem.click()

# Wait for 20 seconds
time.sleep(20)
browser.quit()