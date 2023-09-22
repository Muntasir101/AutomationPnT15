from selenium import webdriver
from selenium.webdriver.common.by import By
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


def upload(driver):
    choose_file_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input#file-upload")))

    file = "E:\\Offline_Batch_15\\18th Class\\Class 18.txt"

    choose_file_button.send_keys(file)

    upload_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input#file-submit")))

    upload_button.click()


def terminate_browser(driver):
    driver.quit()


def main():
    url = "https://the-internet.herokuapp.com/upload"

    driver = launch_browser("firefox")
    navigate_url(driver, url)
    upload(driver)
    #terminate_browser(driver)


if __name__ == "__main__":
    main()
