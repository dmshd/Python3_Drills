# https://techstepacademy.com/trial-of-the-stones
# * Complete all the riddles automatedly
# * Once the Riddle have been solved, click the 'Check Answers' button automatically.
# * Perform an 'assert' to verify that the message 'Trial Complete' has been displayed.
# * On the challenge of the Two Merchants, if you are not yet comfortable enough with
# Python to compare merchant wealth and discover the name dynamically, you may start by
# finding the Web Element representing the highest number and navigating to the
# merchant's name from there using XPATH.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/trial-of-the-stones")

# Riddle of Stone
riddle_of_stone_input = browser.find_element(By.CSS_SELECTOR, "input[id='r1Input']")
riddle_of_stone_answer_submit_butn = browser.find_element(By.XPATH, "//button[@id='r1Btn']")
riddle_of_stone_input.clear()
riddle_of_stone_input.send_keys("rock")
riddle_of_stone_answer_submit_butn.click()

# Riddle of Secrets
riddle_of_secrets_input_xpath_locator = "//input[@id='r2Input']"
riddle_of_secrets_answer_submit_butn_css_locator = "button[id='r2Butn']"
riddle_of_secrets_input = browser.find_element(By.XPATH, riddle_of_secrets_input_xpath_locator)
riddle_of_secrets_input.clear()
riddle_of_secrets_input.send_keys("bamboo")
riddle_of_secrets_answer_submit_butn = browser.find_element(By.CSS_SELECTOR, riddle_of_secrets_answer_submit_butn_css_locator)
riddle_of_secrets_answer_submit_butn.click()

# The Two Merchants
prices_to_compare_locator = "//label[text()='Total Wealth ($):']/following-sibling::p"
prices_elements = browser.find_elements(By.XPATH, prices_to_compare_locator)

# debug to understand the prices_elements, as reference
# print("dir() of price_elements:\n", dir(prices_elements))
# if len(prices_elements) > 1:
#     for elem in prices_elements:
#         print("dir() of individual elem:\n", dir(elem))

prices = []

try:
    for elem in prices_elements:
        prices.append(int(elem.text))
except ValueError:
    print("ValueError: could not convert string to int")

max_price = max(prices)

element_of_richest_marchant = [elem for elem in prices_elements if int(elem.text) == max_price][0]
richest_marchant_name = element_of_richest_marchant.find_element(By.XPATH, "./preceding-sibling::span").text

name_of_the_richest_merchant_input_xpath_locator = "//input[@id='r3Input']"
name_of_the_richest_merchant_input = browser.find_element(By.XPATH, name_of_the_richest_merchant_input_xpath_locator)
name_of_the_richest_merchant_input.clear()
name_of_the_richest_merchant_input.send_keys(richest_marchant_name)

riddle_of_the_two_merchants_answer_submit_butn_css_locator = "button[id='r3Butn']"
riddle_of_the_two_merchants_answer_submit_butn = browser.find_element(By.CSS_SELECTOR, riddle_of_the_two_merchants_answer_submit_butn_css_locator)
riddle_of_the_two_merchants_answer_submit_butn.click()

# Input user to ask if the browser should be closed
input("Press Enter to close the browser...")
browser.quit()
