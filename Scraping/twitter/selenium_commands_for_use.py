from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import logging


class DriverSetup:
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

    def setup_driver(self, url=""):     # enter the URL here
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.option)
        driver.get(url)
        driver.maximize_window()
        return driver

    def open_new_driver_with_brave(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.option)
        return driver


class PageInteractions:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, css_selector):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except Exception as e:
            logging.error(f"Element not found with css selector {css_selector}: {str(e)}")
            return None

    def enter_input(self, css_selector, input_text):
        element = self.find_element(css_selector)
        if element is not None:
            element.send_keys(input_text)

    def click_button(self, css_selector, index=0):
        try:
            buttons = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
            buttons[index].click()
        except Exception as e:
            logging.error(f"Exception occurred while clicking button: {str(e)}")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_element(self, css_selector):
        self.find_element(css_selector)

    def navigate_to(self, url):
        current_url = self.driver.current_url
        modified_url = current_url + url
        self.driver.get(modified_url)

    def get_current_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def scroll_and_sleep(self, sleep_time):
        self.scroll_down()
        time.sleep(sleep_time)

    def check_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def sleep(driver, sleep_time):
        time.sleep(sleep_time)

    def go_to_latest(driver):
        interaction = PageInteractions(driver)
        interaction.add_url_address("")

    def close_driver(driver):
        driver.quit()


class ElementRetrieval:
    def __init__(self, card: WebElement):
        self.card = card

    def get_element_text_xpath(self, xpath: str) -> str:
        try:
            element = self.card.find_element(By.XPATH, xpath)
            return element.text
        except Exception as e:
            logging.error(f"An error occurred when finding element with XPath {xpath}: {str(e)}")
            return None

    def get_element_text_css(self, css_selector: str) -> str:
        try:
            element = self.card.find_element(By.CSS_SELECTOR, css_selector)
            return element.text
        except Exception as e:
            logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
            return None

    def get_src_element_url_xpath(self, xpath_selector: str) -> str:
        try:
            element = self.card.find_element(By.XPATH, xpath_selector)
            return element.get_attribute('src')
        except Exception as e:
            logging.error(f"An error occurred when finding element with selector {xpath_selector}: {str(e)}")
            return None

    def get_src_element_url_css(self, css_selector: str) -> str:
        try:
            element = self.card.find_element(By.CSS_SELECTOR, css_selector)
            return element.get_attribute('src')
        except Exception as e:
            logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
            return None

    def get_element_attribute_xpath(self, xpath: str, attribute: str) -> str:
        try:
            element = self.card.find_element(By.XPATH, xpath)
            return element.get_attribute(attribute)
        except Exception as e:
            logging.error(f"An error occurred when finding element with XPath {xpath}: {str(e)}")
            return None

    def get_herf_element_attribute_css(self, css_selector: str) -> str:
        try:
            element = self.card.find_element(By.CSS_SELECTOR, css_selector)
            return element.get_attribute('href')
        except Exception as e:
            logging.error(f"An error occurred when finding element with selector {css_selector}: {str(e)}")
            return None
