from selenium import webdriver
from selenium.webdriver.common.by import By

# Headless
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


driver.get("https://www.browserstack.com/")
element = driver.find_element(By.NAME, "query")
assert element.is_enabled()
driver.quit()