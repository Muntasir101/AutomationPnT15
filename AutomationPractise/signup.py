import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.maximize_window()

driver.get("https://automationexercise.com/login")

driver.find_element(By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[2]").send_keys(
    "Avi")
# time.sleep(1)
driver.find_element(By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[3]").send_keys(
    "deyiiyguoyfa6732@vip4e.com")
# time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()

# time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='id_gender1']").click()
# time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Avi@2001")

time.sleep(1)
dropdown = driver.find_element(By.XPATH, "//select[@id='days']")

# dropdown element day
select = Select(dropdown)

select.select_by_index(19)

# time.sleep(1)

dropdown = driver.find_element(By.XPATH, "//select[@id='months']")

# dropdown element day
select = Select(dropdown)

select.select_by_visible_text('November')


# time.sleep(1)

dropdown = driver.find_element(By.XPATH, "//select[@id='years']")

# dropdown element day
select = Select(dropdown)

select.select_by_visible_text('2001')

# time.sleep(1)


driver.find_element(By.XPATH, "//input[@id='newsletter']").click()

# time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='optin']").click()



# time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Avi")
# time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Avi")
# time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='company']").send_keys("Avi")
# time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#address1").send_keys("Avi")
# time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='address2']").send_keys("AVi")
# time.sleep(1)

dropdown = driver.find_element(By.XPATH, "//select[@id='country']")

# dropdown element day
select = Select(dropdown)

select.select_by_visible_text('India')

# time.sleep(1)


driver.find_element(By.XPATH, "//input[@id='state']").send_keys("AVi")
# time.sleep(1)



driver.find_element(By.XPATH, "//input[@id='city']").send_keys("AVi")
# time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("AVi")
# time.sleep(1)


driver.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("AVi")
# time.sleep(1)

driver.find_element(By.XPATH, "//button[contains(text(),'Create Account')]").click()
# time.sleep(1)