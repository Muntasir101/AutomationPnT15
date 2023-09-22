"""
1. Wait for specific amount of time for an element to appear for specified condition.
Throw error NoSuchElementException

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username")))

password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password")))

login_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))

if username.is_displayed() == True and username.is_enabled() == True == True:
    username.clear()
    username.send_keys("Admin")
else:
    print("Bug Found !!!!")

if password.is_displayed() == True and password.is_enabled() == True:
    password.clear()
    password.send_keys("admin123")

login_text = login_btn.text
if login_text == "Login":
    print("Login Text Matched")
else:
    print("Login Text Not Matched.Bug Found!!!!")
