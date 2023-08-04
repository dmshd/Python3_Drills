# trial_of_the_stones_solution.py

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# Riddle of Stone
stone_input = browser.find_element(By.ID, "r1Input")
stone_answer_butn = browser.find_element(By.CSS_SELECTOR, "button#r1Btn")
stone_result = browser.find_element(By.CSS_SELECTOR, "div#passwordBanner > h4")

# Riddle of Secrets
secrets_input = browser.find_element(By.CSS_SELECTOR, "input[id='r2Input']")
secrets_answer_butn = browser.find_element(By.CSS_SELECTOR, "button#r2Butn")

# Two Merchants
# Simple Approach

richest_merchant_name = browser.find_element(By.XPATH, "//p[text()='3000']")