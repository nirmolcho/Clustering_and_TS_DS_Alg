from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import logging


def setup_driver():
    option = webdriver.ChromeOptions()
    option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get("https://twitter.com/")
    driver.maximize_window()
    return driver


def open_new_driver_with_brave():
    option = webdriver.ChromeOptions()
    option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    return driver


# commends while scrapping
def add_url_address(driver):
    current_url = driver.current_url
    modified_url = current_url + ""  # add url here
    driver.get(modified_url)


def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '[data-testid="tweet"]')))


def wait_for_tweet_update(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="tweet"]')))
    except WebDriverException:
        print("Tweets did not appear!, Try setting headless=False to see what is happening")


def wait_for_user_profile_update(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="primaryColumn"]')))
    except WebDriverException:
        print("Tweets did not appear!, Try setting headless=False to see what is happening")


# get element using XPATH
def get_element_text_xpath(card: WebElement, xpath: str) -> str:
    try:
        element = card.find_element(By.XPATH, xpath)
        return element.text
    except Exception as e:
        logging.error(f"An error occurred when finding element with XPath {xpath}: {str(e)}")
        return None


def get_src_element_url_XPath(card: WebElement, xpath_selector: str) -> str:
    try:
        element = card.find_element(By.XPATH, xpath_selector)
        return element.get_attribute('src')
    except Exception as e:
        logging.error(f"An error occurred when finding element with selector {xpath_selector}: {str(e)}")
        return None


def get_element_attribute_xpath(card: WebElement, xpath: str, attribute: str) -> str:
    try:
        element = card.find_element(By.XPATH, xpath)
        return element.get_attribute(attribute)
    except Exception as e:
        logging.error(f"An error occurred when finding element with XPath {xpath}: {str(e)}")
        return None


# get element using CSS
def get_element_text_CSS(card: WebElement, css_selector: str) -> str:
    try:
        element = card.find_element(By.CSS_SELECTOR, css_selector)
        return element.text
    except Exception as e:
        logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
        return None


def get_src_element_url_CSS(card: WebElement, css_selector: str) -> str:
    try:
        element = card.find_element(By.CSS_SELECTOR, css_selector)
        return element.get_attribute('src')
    except Exception as e:
        logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
        return None


def get_het_element_attribute_CSS(card: WebElement, css_selector: str) -> str:
    try:
        element = card.find_element(By.CSS_SELECTOR, css_selector)
        return element.get_attribute('href')
    except Exception as e:
        logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
        return None
