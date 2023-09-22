from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configure logging
log_file = "Selenium_log.txt"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[logging.FileHandler(log_file)])
logger = logging.getLogger(__name__)


def launch_browser():
    logger.info("------------------------------")
    logger.info(f"Launching browser")
    return webdriver.Chrome()


def navigate_url(driver, url):
    driver.maximize_window()
    logger.info(f"Navigating to {url}")
    driver.get(url)


def user_signup(driver):
    fake = Faker()
    random_email = fake.email()
    username = fake.name()

    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[2]")))

    username_field.send_keys(username)
    logger.info(f"Username Typed: {username}")

    driver.find_element(By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[3]").send_keys(
        random_email)
    logger.info(f"Email Typed: {random_email}")

    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
    logger.info(f"Signup Button Clicked")


def terminate_browser(driver):
    logger.info(f"Terminating browser.")
    driver.quit()


def main():
    url = "https://automationexercise.com/login"

    driver = launch_browser()
    navigate_url(driver, url)
    user_signup(driver)
    terminate_browser(driver)


if __name__ == "__main__":
    main()
