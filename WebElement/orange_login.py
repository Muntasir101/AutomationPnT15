from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_btn = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

username.send_keys("Admin")
time.sleep(3)
password.send_keys("admin123")
time.sleep(2)
login_btn.click()
time.sleep(5)



