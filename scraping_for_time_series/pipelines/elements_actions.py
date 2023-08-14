import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from utils.driver_manager import DriverManager
import logging


class FindElements:
    def __init__(self, driver):
        self.driver = driver
        self.driver_manager = DriverManager(self.driver)

    def send_keys_using_CSS_SELECTOR(self, element_path: str, searchWord: str):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f'{element_path}'))
            )
            part_len = len(searchWord) // 3
            parts = [searchWord[i:i + part_len] for i in range(0, len(searchWord), part_len)]
            for part in parts:
                element.send_keys(part)
                time.sleep(0.3)
            element.send_keys(Keys.RETURN)
        except Exception as e:
            print("Exception occurred in 'send_keys_using_CSS_SELECTOR:' ", str(e))

    def send_keys_using_XPATH(self, element_path: str, searchWord: str):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f'{element_path}'))
            )
            element.send_keys(searchWord)
            time.sleep(0.1)
            element.send_keys(Keys.ENTER)
        except Exception as e:
            print("Exception occurred in 'send_keys_using_XPATH:' ", str(e))

    def check_if_element_exist_with_CSS_SELECTOR(self, element_: str):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, f'{element_}')))
        except WebDriverException:
            print("Element not found")

    def check_if_element_exist_with_XPATH(self, element_: str):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, f'{element_}')))
        except WebDriverException:
            print("Element not found")

    def wait_for_element_update_CSS(self, element_: str):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, f'{element_}')))
        except WebDriverException:
            print("Try setting headless=False to see what is happening : 'wait_for_element_update_CSS' ")

    def wait_for_element_update_XPATH(self, element_: str) -> object:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, f'{element_}')))
        except WebDriverException:
            print("Element not found")

    def click_button_with_CSS_SELECTOR(self, element_: str):
        try:
            self.driver.delete_all_cookies()
            button = self.driver.find_element(By.CSS_SELECTOR, f'{element_}')
            button.click()
        except NoSuchElementException:
            print("Button element not found with 'click_button_with_CSS_SELECTOR' ")
        except WebDriverException:
            print("Try setting headless=False to see what is happening 'click_button_with_CSS_SELECTOR'")

    def click_button_with_XPATH(self, element_: str):
        try:
            button = self.driver.find_element(By.XPATH, f'{element_}')
            button.click()
        except NoSuchElementException:
            print("Button element not found with 'click_button_with_XPATH' ")
        except WebDriverException:
            print("Try setting headless=False to see what is happening 'click_button_with_XPATH' ")


class ExtractFromElements:
    @staticmethod
    def get_element_text_XPATH(card: WebElement, xpath: str) -> str:
        try:
            element = card.find_element(By.XPATH, xpath)
            return element.text
        except Exception as e:
            logging.error(f"An error occurred when finding element with XPath {xpath}: {str(e)}")
            return None

    @staticmethod
    def get_element_attribute_XPATH(card: WebElement, xpath: str, attribute: str) -> str:
        try:
            element = card.find_element(By.XPATH, xpath)
            return element.get_attribute(attribute)
        except Exception as e:
            logging.error(f"An error occurred when finding element with XPath {xpath}: {str(e)}")
            return None

    @staticmethod
    def get_element_text_CSS(card: WebElement, css_selector: str) -> str:
        try:
            element = card.find_element(By.CSS_SELECTOR, css_selector)
            return element.text
        except Exception as e:
            logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
            return None

    @staticmethod
    def get_element_url_CSS(card: WebElement, css_selector: str) -> str:
        try:
            element = card.find_element(By.CSS_SELECTOR, css_selector)
            return element.get_attribute('src')
        except Exception as e:
            logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
            return None

    @staticmethod
    def get_element_attribute_CSS_herf(card: WebElement, css_selector: str) -> str:
        try:
            element = card.find_element(By.CSS_SELECTOR, css_selector)
            return element.get_attribute('href')
        except Exception as e:
            logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
            return None

    @staticmethod
    def get_element_attribute_XPATH_herf(card: WebElement, css_selector: str) -> str:
        try:
            element = card.find_element(By.XPATH, css_selector)
            return element.get_attribute('href')
        except Exception as e:
            logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
            return None
