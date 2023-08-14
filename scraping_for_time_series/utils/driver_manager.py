import logging
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class DriverManager:
    def __init__(self, brave_path):
        self.brave_path = brave_path
        self.drivers = []
        self.current_driver = 0
        self.timeout = 5
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
            'Windows 10/ Edge browser: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
            'Windows 7/ Chrome browser: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
            'Mac OS X10/Safari browser: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
            'Linux PC/Firefox browser: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
            'Chrome OS/Chrome browser: Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        ]
        self.headers_dict = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                                       "image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
                             'Cookie':
                                 '__uzma=07595de8-3ac0-4269-b643-6b9c854662d4; __uzmb=1629217912; __uzme=8731; '
                                 'abTestKey=87; canary=never;'
                                 '_gid=GA1.3.727512284.1629218142; server_env=production; y2018-2-cohort=10; '
                                 'leadSaleRentFree=24;'
                                 'y2_cohort_2020=22; use_elastic_search=1; '
                                 '_gac_UA-708051-1=1.1629218145'
                                 '.EAIaIQobChMIwej5tL648gIVE9Z3Ch1WbQA8EAAYASAAEgJhqPD_BwE;'
                                 '__gads=ID=d4f424dd8ad50a10:T=1629218144:S=ALNI_Mb4n1Ah7WsVMwvIJ8BZ-MGibKd9Hg; '
                                 '_hjid=2ed38dd8-5c19-4b5f-9892-92c26d8fad8c; _hjFirstSeen=1; '
                                 '_fbp=fb.2.1629218147934.408187103;'
                                 '_hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; '
                                 'bc.visitor_token=6833436205214232576;'
                                 'rdw_storereferer=https://www.yad2.co.il/realestate/commercial?topArea=2&area=1&city'
                                 '=5000&dealType=0'
                                 '&property=13; _ga_GQ385NHRG1=GS1.1.1629218144.1.1.1629218954.54; '
                                 '_ga=GA1.3.1134226525.1629218142;'
                                 'favorites_userid=gbd1554579504; __uzmc=511456726626; __uzmd=1629218968',
                             'User-Agent':
                                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ('
                                           'KHTML, like Gecko)'
                                           'Chrome/92.0.4515.131 Safari/537.36'}

        self.proxys = ['34.87.130.84:8080',
                       '117.54.114.103:80',
                       '66.94.99.30:443',
                       '202.166.220.143:55443',
                       '61.29.96.146:80',
                       '113.161.131.43:80']

    def start_drivers(self):
        user_agent = random.choice(self.user_agents)
        proxy = random.choice(self.proxys)
        option = webdriver.ChromeOptions()
        option.binary_location = self.brave_path
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        self.drivers.append(driver)

    def get_driver(self):
        driver = self.drivers[self.current_driver]
        return driver

    def quit_drivers(self):
        for driver in self.drivers:
            driver.quit()
