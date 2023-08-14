import time
from urllib.parse import urlencode
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage
from pipelines.pipelines import Pipeline
from utils.driver_manager import DriverManager
from pipelines.elements_actions import FindElements
from page_objects.paths import PathsFunctions
from utils.general_funcs import GeneralFuncs
from pytiktok import BusinessAccountApi


class LoginSpider:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.pipe = Pipeline()
        self.driver_manager = DriverManager(self.driver)
        self.element = FindElements(self.driver)
        self.get_path = PathsFunctions()
        self.general_funcs = GeneralFuncs()
        #self.user_email1 = self.pipe.get_user_email()
        #self.user_password1 = self.pipe.get_user_password()
        self.user_email = 'dronteamsend@gmail.com'
        self.user_password = 'Pa##w0rd'
        self.API_KEY_proxy = 'fe2b6ad58482ff57e9a6a90a446073fd'
        self.TIKTOK_API_KEY = 'awxbrimvhm200dlm'

    def get_scraperapi_url(self, url):
        payload = {'api_key': self.API_KEY, 'url': url}
        proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
        return proxy_url

    def login_website(self):
        url = ''
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.refresh()

    def login_user(self):
        # wait for email input
        self.general_funcs.wrapper(self.element.wait_for_element_update_CSS(
            self.get_path.username_CSS_SELECTOR()),
            self.element.wait_for_element_update_XPATH(self.get_path.username_XPATH()))

        time.sleep(2)
        # send keys to email input
        self.general_funcs.wrapper(self.element.send_keys_using_CSS_SELECTOR(self.get_path.username_CSS_SELECTOR(),
                                                                             self.user_email),
                                   self.element.send_keys_using_XPATH(self.get_path.username_XPATH(),
                                                                      self.user_email))
        time.sleep(2)
        # wait for password input
        self.general_funcs.wrapper(
            self.element.wait_for_element_update_CSS(self.get_path.password_CSS_SELECTOR()),
            self.element.wait_for_element_update_XPATH(self.get_path.password_XPATH()))

        time.sleep(2)

        # send keys to password input
        self.general_funcs.wrapper(
            self.element.send_keys_using_CSS_SELECTOR(self.get_path.password_CSS_SELECTOR(),
                                                      self.user_password),
            self.element.send_keys_using_XPATH(self.get_path.password_XPATH(),
                                               self.user_password))