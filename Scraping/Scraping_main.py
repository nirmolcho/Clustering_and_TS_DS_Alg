import time
import urllib3
import warnings
import pandas as pd
import concurrent.futures
import logging
from datetime import datetime, timedelta
from login_account import Automator, get_user_search_term
from information_scraper import TweetScraper, UserProfileScraper, ProfileProcessor, get_final_twitter
from selenium_commands_for_use import DriverSetup, PageInteractions, ElementRetrieval
from general_classes import Timer, Config


def main():
    # timing
    total_timer = Timer()
    login_timer = Timer()
    scraping_data_timer = Timer()
    scraping_user_data_timer = Timer()

    # global variables
    config = Config()
    driver = DriverSetup()
    total_timer.start_timer()
    driver.setup_driver()
    scrape_elements = TweetScraper()
    scrape_user_profile = UserProfileScraper()

    login_timer.start_timer()
    automator = Automator(driver)
    automator.login_user(config.user_name, config.password)
    login_timer.end_timer()

    automator.search_box(driver, get_user_search_term())

    scraping_data_timer.start_timer()
    scrape_elements.scrape_tweets(driver)
    scraping_data_timer.end_timer()

    scraping_user_data_timer.start_timer()
    scrape_user_profile.scrape_user_profile(tdf, driver2, last_index)
    scraping_user_data_timer.end_timer()

    total_timer.end_timer()

    get_final_twitter()

    return total_timer.time, login_timer.time, scraping_data_timer.time, scraping_user_data_timer.time


if __name__ == "__main__":
    total_time, login_time, scraping_data_time, scraping_user_data_time = main()
    print("Runtime of total program                   : ", total_time)
    print("Runtime of login                           : ", login_time)
    print("Runtime of scraping data                   : ", scraping_data_time)
    print("Runtime of scraping user data              : ", scraping_user_data_time)
