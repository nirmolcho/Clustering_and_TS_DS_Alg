from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.paths import PathsFunctions
from utils.scheduler import Scheduler
from pipelines.get_data_from_scraping import ScrapingData


class ScrollManager:
    def __init__(self, driver):
        self.driver = driver
        self.driver_manager = DriverManager(self.driver)
        self.timer = Scheduler()
        self.get_data = ScrapingData(self.driver)

    def get_current_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_until_element(self, element_path: str):
        element_found_path = None
        try:
            element_found_path = self.driver.find_element_by_xpath(element_path)
        except Exception as e:
            print("Exception occurred in 'scroll_until_element:' ", str(e))
            return

        while true:
            current_height = self.get_current_height()
            self.scroll()
            time.sleep(1)
            new_height = self.get_current_height()
            if element_found_path.is_displayed():
                break
            if current_height == new_height:
                break

    def scroll_until_got_all_elements(self, max_elements: int, time_of_data_scraping: function):
        while True:
            current_height = self.get_current_height()
            num_of_scraped_elements, time_to_scrape = time_of_data_scraping()
            self.scroll()
            time.sleep(time_to_scrape)
            new_height = self.get_current_height()
            if current_height == new_height:
                break
            elif max_elements >= num_of_scraped_elements:
                break

