import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def launch_browser(browser_name):
    if browser_name == 'chrome':
        return webdriver.Chrome()
    else:
        return webdriver.Firefox()


def navigate_url(driver, url):
    driver.maximize_window()
    driver.get(url)


def user_signup(driver):
    fake = Faker()

    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[2]")))

    driver.find_element(By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[3]").send_keys(
        fake.email())

    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()

    driver.find_element(By.XPATH, "//input[@id='id_gender1']").click()
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Avi@2001")

    dropdown = driver.find_element(By.XPATH, "//select[@id='days']")

    day_select = Select(dropdown)

    day_select.select_by_index(19)

    month_dropdown = driver.find_element(By.XPATH, "//select[@id='months']")

    select = Select(month_dropdown)

    select.select_by_visible_text('November')

    dropdown = driver.find_element(By.XPATH, "//select[@id='years']")

    year_select = Select(dropdown)

    year_select.select_by_visible_text('2001')

    driver.find_element(By.XPATH, "//input[@id='newsletter']").click()

    driver.find_element(By.XPATH, "//input[@id='optin']").click()

    driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Avi")

    driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Avi")
    driver.find_element(By.XPATH, "//input[@id='company']").send_keys("Avi")
    driver.find_element(By.CSS_SELECTOR, "#address1").send_keys("Avi")
    driver.find_element(By.XPATH, "//input[@id='address2']").send_keys("AVi")

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


def terminate_browser(driver):
    driver.quit()


def main():
    url = "https://automationexercise.com/login"

    driver = launch_browser("chrome")
    navigate_url(driver, url)
    user_signup(driver)
    terminate_browser(driver)


if __name__ == "__main__":
    main()
