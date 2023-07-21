import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium_commands_for_use import wait_for_element_update, enter_input, click_button
from selenium.webdriver.support import expected_conditions as EC


class Automator:
    def __init__(self, driver):
        self.driver = driver

    def login_user(self, username, password):
        wait_for_element_update(self.driver)
        click_button(self.driver, '')   # should look like this a[data-testid="login"]
        enter_input(self.driver, 'session_key', username)
        enter_input(self.driver, '', password)
        click_button(self.driver, '')

    def search_box(self, search_word):
        wait_for_element_update(self.driver)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]'))
            )
            element.send_keys(search_word)
            time.sleep(0.1)
        except Exception as e:
            print("Exception occurred: ", str(e))

        search_in_twitter = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')
        search_in_twitter.send_keys(Keys.ENTER)
        time.sleep(1)


def get_user_search_term():
    print("What are you looking for? ")
    search_term = input()
    return search_term
