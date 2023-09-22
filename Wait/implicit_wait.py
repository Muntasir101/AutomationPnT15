"""
1. Wait for specific amount of time for an element to appear.
Throw error NoSuchElementException
2. This is global wait time
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(10)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_btn = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

username_display_state = username.is_displayed()
print(username_display_state)

username_enabled_state = username.is_enabled()
print(username_enabled_state)

if username_display_state == True and username_enabled_state == True:
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
