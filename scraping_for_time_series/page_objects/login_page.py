import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pipelines.elements_actions import FindElements
from pipelines.pipelines import Pipeline
from page_objects.paths import PathsFunctions
from utils.driver_manager import DriverManager
from utils.general_funcs import GeneralFuncs


def wrapper(func1, func2):
    if callable(func1) and callable(func2):
        try:
            return func1()
        except Exception as e:
            print(f"Function {func1.__name__} failed with error: {e}. Trying function {func2.__name__}...")
            try:
                return func2()
            except Exception as e:
                print(f"Function {func2.__name__} also failed with error: {e}")
                return None
    else:
        return None


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.element = FindElements(self.driver)
        self.pipe = Pipeline()
        self.get_path = PathsFunctions()
        self.driver_manager = DriverManager(self.driver)
        self.general_funcs = GeneralFuncs()

    def search(self, search_term: object) -> object:
        time.sleep(self.driver_manager.timeout)
        self.general_funcs.wrapper(
            self.element.wait_for_element_update_CSS(self.get_path.search_general_CSS_SELECTOR()),
            self.element.wait_for_element_update_XPATH(self.get_path.search_general_XPATH()))
        time.sleep(self.driver_manager.timeout)
        self.general_funcs.wrapper(
            self.element.send_keys_using_CSS_SELECTOR(self.get_path.search_general_CSS_SELECTOR(),
                                                      search_term),
            self.element.send_keys_using_XPATH(self.get_path.search_general_XPATH(),
                                               search_term))




