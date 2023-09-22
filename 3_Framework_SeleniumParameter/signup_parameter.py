import argparse
import json

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


def launch_browser(headless=False):
    logger.info("------------------------------")
    logger.info(f"Launching browser")
    # read configuration from JSON file
    with open('config.json', "r") as config_file:
        config = json.load(config_file)

        browser = config['browser']

        if browser == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            if headless:
                chrome_options.add_argument("--headless")
            return webdriver.Chrome(options=chrome_options)
        elif browser == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            if headless:
                firefox_options.add_argument("--headless")
            return webdriver.Firefox(options=firefox_options)


def navigate_url(driver, url):
    logger.info(f"Navigating to {url}")
    driver.get(url)


def user_signup(driver):
    fake = Faker()
    random_email = fake.email()
    username = fake.name()

    # read configuration from JSON file
    with open('locators.json', "r") as config_file:
        config = json.load(config_file)

    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, config['username_field_CSS'])))

    username_field.send_keys(username)
    logger.info(f"Username Typed: {username}")

    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']")))

    email_field.send_keys(random_email)
    logger.info(f"Email Typed: {random_email}")

    signup_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button[data-qa='signup-button']")))

    signup_button.click()
    logger.info(f"Signup Button Clicked")


def terminate_browser(driver):
    logger.info(f"Terminating browser.")
    driver.quit()


def main():
    # create an argument parser
    parser = argparse.ArgumentParser(description="Selenium Script with Parameters")
    parser.add_argument("--config", default="config.json", help="path to the configuration JSON file")
    args = parser.parse_args()

    # read configuration from JSON file
    with open('config.json', "r") as config_file:
        config = json.load(config_file)

        url = config['url']
        headless = config['headless']

    driver = launch_browser(headless=headless)
    navigate_url(driver, url)
    user_signup(driver)
    terminate_browser(driver)


if __name__ == "__main__":
    main()
