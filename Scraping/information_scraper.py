import re
import os
import csv
import time
import urllib3
import logging
import pandas as pd
from datetime import date, datetime
from selenium.webdriver.common.by import By
from typing import Any, Callable, Optional
from selenium_commands_for_use import PageInteractions, ElementRetrieval, DriverSetup
from cleaning_the_data import clean_tweets_bio_data, clean_tweets_data
import general_classes
from organized_data import cleaningDataset, final_merge, looking_for_missing, get_missing_profiles, \
                           get_user_profile_info_to_csv, merge_missing


class SafeWrapper:
    @staticmethod
    def wrap(func: Callable[..., Any]) -> Callable[..., Optional[Any]]:
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f"An error occurred in function {func.__name__}: {str(e)}")
                return None
        return inner


class TweetScraper:

    def __init__(self, driver):
        self.driver = driver
        self.config = general_classes.Config()
        self.element_retrieval = ElementRetrieval(driver)

    def getTweetsInfo(self, driver):
        config = general_classes.Config()
        element_retrieval = ElementRetrieval(driver)
        wait_for_element_update(driver)
        tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
        selectors_css = {
            'tweet_used': '',       #looks like this: div[data-testid="User-Name"]
            'tweet_text': '',       #looks like this: div[data-testid="tweetText"]
            'retweet_count': '',    #looks like this: div[data-testid="retweet"]
            'like_count': '',       #looks like this: div[data-testid="like"]
            'reply_count': '',      #looks like this: div[data-testid="reply"]
            'view_count': "",       #looks like this: a[aria-label*=' Views'] span span
        }
        selectors_css_url = {
            'image_url': '',        #looks like this: div[data-testid="tweetPhoto"] img
            'video_url': '',        #looks like this: div[data-testid="videoComponent"] video
            'url_attached': ''      #looks like this: div[data-testid="card.layoutLarge.media"] img
        }
        selectors_css_herf = {
            'tweet_link': '.css-4rbku5.css-18t94o4.css-901oao',
        }

        scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
        for card in tweets:
            new_tweet = {**{key: element_retrieval.get_element_text_css(card, selectors) \
                            for key, selector in selectors_css.items()},
                         **{key: element_retrieval.get_src_element_url_css(card, selectors) \
                            for key, selector in selectors_css_url.items()},
                         **{key: element_retrieval.get_herf_element_attribute_css(card, selectors) \
                            for key, selector in selectors_css_herf.items()},
                         'scrape_time': scrape_time}
            config.tweet_data.append(new_tweet)
            tweet_count += 1
            if tweet_count >= config.max_elements:
                break

        df = pd.DataFrame(config.tweet_data)
        df.to_csv("elements_scraped.csv", index=False)
        return tweet_count

    def scrape_tweets(driver):
        config = general_classes.Config()
        element_retrieval = PageInteractions(driver)
        while True:
            current_height = element_retrieval.get_current_height(driver)
            timer = Timer()
            timer.start_timer()
            result = getTweetsInfo(driver)
            timer.end_timer()
            execution_time = timer.time
            element_retrieval.sleep_time = max(0, config.time_sleep - execution_time)
            element_retrieval.sleep(driver, sleep_time)
            element_retrieval.scroll(driver, sleep_time)
            element_retrieval.sleep(driver, sleep_time)
            new_height = element_retrieval.check_height(driver)
            element_retrieval.sleep(driver, sleep_time)
            if new_height == current_height:
                element_retrieval.go_to_latest(driver)
            elif result >= config.max_elements or config.tweet_count >= config.max_elements:
                element_retrieval.close_driver(driver)
                break


class BioScraper:
    def __init__(self, driver):
        self.driver = driver
        self.config = general_classes.Config()
        self.element_retrieval = ElementRetrieval(driver)

    def get_bio_info(self):
        config = general_classes.Config()
        element_retrieval = ElementRetrieval(driver)
        tweets = driver.find_elements(By.CSS_SELECTOR, 'div.css-1dbjc4n svg[aria-label="Verified account"]')
        current_url = driver.current_url
        userId = current_url.rsplit('/', 1)[-1]
        selectors_css = {
            'verified_account': '', # looks like this: div.css-1dbjc4n svg[aria-label="Verified account"]
        }

        selectors_xpath = {
            'user_location': '',    # looks like this: //span[@data-testid="UserLocation"]/span[@class="css-901oao
                                    # css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]

            'following': "",        # looks like this: //span[contains(text(), 'Following')]/ancestor::a/span

            'followers': "",        # looks like this: //span[contains(text(), 'Followers')]/ancestor::a/span

            'join_date': '',        # looks like this: //span[@data-testid="UserJoinDate"]/span[@class="css-901oao
                                    # css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]

            'user_description': "", # looks like this: //div[@data-testid='UserDescription']
        }

        selectors_xpath_element = {
            'user_profile_pic': ""   # looks like this: //img[@class='css-9pa8cd']
        }
        file_exists = os.path.isfile("the_tweets_user_bio.csv")
        if file_exists:
            df_existing = pd.read_csv("the_tweets_user_bio.csv")
            user_bio_data = df_existing.to_dict('records')

        for card in tweets:
            new_tweet = {'userid': userId,
                         **{key: element_retrieval.get_element_text_css(card, selector) for key, selector in selectors_css.items()},
                         **{key: element_retrieval.get_element_text_xpath(card, selector) for key, selector in selectors_xpath.items()},
                         **{key: element_retrieval.get_element_attribute_xpath(card, selector, "src") for key, selector in
                            selectors_xpath_element.items()}
                         }
            try:
                verified_element = card.find_elements(By.CSS_SELECTOR, selectors_css['verified_account'])
                new_tweet['verified_account'] = 1 if len(verified_element) > 0 else 0

            except:
                pass

            if new_tweet not in user_bio_data:
                user_bio_data.append(new_tweet)

        df = pd.DataFrame(user_bio_data)
        df.to_csv("user_bio.csv", index=False)


class ProfileProcessor:
    def __init__(self, driver):
        self.driver = driver
        self.config = general_classes.Config()

    def process_user_url(self, url):
        config = general_classes.Config()
        time.sleep(config.time_sleep_for_profile - 2)
        self.driver.get(url)
        start_time = time.time()
        wait_for_element_update(self.driver)
        self.get_bio_info()  # "()" has been added to call the method
        end_time = time.time()
        time_takes_to_finish = start_time - end_time
        sleep_time = max(0, config.time_sleep_for_profile - time_takes_to_finish)
        time.sleep(sleep_time)


class UserProfileScraper:
    def __init__(self, driver):
        self.driver = driver
        self.config = general_classes.Config()
        self.profile_processor = ProfileProcessor(driver)

    def get_data_from_new_url(self, user_urls_df):
        for url in user_urls_df:
            if url not in self.config.visited_urls:
                self.bio_scraper.process_user_url(url)
                self.config.visited_urls.add(url)

    def get_new_user_url(self, df):
        for _, row in df.iterrows():
            user_url = f"/{row['userid']}" # change the website URL
            if user_url not in self.config.user_urls:
                self.config.user_urls.add(user_url)
        return list(self.config.user_urls)

    def scrape_user_profile(self, df, last_index):
        cleaningDataset(df)
        user_url_df = self.get_new_user_url(df)
        user_url_df = user_url_df[last_index:]
        self.get_data_from_new_url(user_url_df)
        return last_index


def get_final_twitter():
    final_merge(clean_tweets_data(), clean_tweets_bio_data())
