import re
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pipelines.elements_actions import FindElements
from pipelines.pipelines import Pipeline
from page_objects.get_feed_data import FeedData
from page_objects.get_profile_bio_data import ProfileData
from utils.scheduler import Scheduler


class ScrapingData:
    def __init__(self, driver):
        self.driver = driver
        self.element = FindElements(self.driver)
        self.pipe = Pipeline()
        self.get_feed_path = FeedData()
        self.get_user_bio_data = ProfileData()
        self.timer = Scheduler()

    @staticmethod
    def _get_text_or_attr(card, selectors, get_func, default_func):
        for key, selector in selectors.items():
            val = get_func(card, selector)
            if val is not None:
                return key, val
        for key, selector in selectors.items():
            val = default_func(card, selector)
            return key, val
        return None, None

    def get_feed_data(self, max_num_of_scraping):
        elements = self.driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
        selectors = {
            'css': {
                'text': {
                    'user_name': self.get_feed_path.user_name_CSS_SELECTOR(),
                    'num_of_likes': self.get_feed_path.num_of_likes_CSS_SELECTOR(),
                    'num_of_comments': self.get_feed_path.num_of_comments_CSS_SELECTOR(),
                    'num_of_bookmark': self.get_feed_path.num_of_bookmark_CSS_SELECTOR(),
                    'num_of_shears': self.get_feed_path.num_of_shears_CSS_SELECTOR(),
                    'video_hashtags': self.get_feed_path.video_hashtags_CSS_SELECTOR(),
                },
                'herf': {
                    'vid_id': self.get_feed_path.vid_id_CSS_SELECTOR(),
                }
            },
            'xpath': {
                'text': {
                    'user_name': self.get_feed_path.user_name_XPATH(),
                    'num_of_likes': self.get_feed_path.num_of_likes_XPATH(),
                    'num_of_comments': self.get_feed_path.num_of_comments_XPATH(),
                    'num_of_bookmark': self.get_feed_path.num_of_bookmark_XPATH(),
                    'num_of_shears': self.get_feed_path.num_of_shears_XPATH(),
                    'video_hashtags': self.get_feed_path.video_hashtags_XPATH(),
                },
                'herf': {
                    'vid_id': self.get_feed_path.vid_id_XPATH(),
                }
            }
        }

        scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.timer.start_timer()
        for card in elements:
            new_element = {}
            for style in ['css', 'xpath']:
                for el_type, funcs in zip(['text', 'herf'],
                                          [(self.element.get_element_text_CSS, self.element.get_element_text_XPATH), (
                                          self.element.get_element_attribute_CSS_herf,
                                          self.element.get_element_attribute_XPATH_herf)]):
                    key, val = self._get_text_or_attr(card, selectors[style][el_type], *funcs)
                    if key is not None:
                        new_element[key] = val
            new_element['scrape_time'] = scrape_time
            self.pipe.feed_items.append(new_element)
            self.pipe.num_of_elements_collected += 1
            self.timer.stop_timer()
            time_scraping_one_element = self.timer.get_elapsed_time()
            if self.pipe.num_of_elements_collected >= max_num_of_scraping:
                break

        df = pd.DataFrame(self.pipe.feed_items)
        df.to_csv("feed_scraped.csv", index=False)
        return len(self.pipe.feed_items), time_scraping_one_element

    def get_user_bio_data(self,max_num_of_scraping):

        elements = self.driver.find_elements(By.CSS_SELECTOR, '')
        selectors = {
            'css': {
                'text': {
                    'user_name': self.get_user_bio_data.user_name_CSS_SELECTOR(),
                    'num_of_following': self.get_user_bio_data.num_of_following_CSS_SELECTOR(),
                    'num_of_followers': self.get_user_bio_data.num_of_followers_CSS_SELECTOR(),
                    'total_num_of_likes': self.get_user_bio_data.total_num_of_likes_CSS_SELECTOR(),
                    'user_description': self.get_user_bio_data.user_description_CSS_SELECTOR(),
                },
                'herf': {
                }
            },
            'xpath': {
                'text': {
                    'user_name': self.get_user_bio_data.user_name_XPATH(),
                    'num_of_following': self.get_user_bio_data.num_of_following_XPATH(),
                    'num_of_followers': self.get_user_bio_data.num_of_followers_XPATH(),
                    'total_num_of_likes': self.get_user_bio_data.total_num_of_likes_XPATH(),
                    'user_description': self.get_user_bio_data.user_description_XPATH(),
                },
                'herf': {
                }
            }
        }
        scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.timer.start_timer()
        for card in elements:
            new_element = {}
            for style in ['css', 'xpath']:
                for el_type, funcs in zip(['text', 'herf'],
                                          [(self.element.get_element_text_CSS, self.element.get_element_text_XPATH), (
                                          self.element.get_element_attribute_CSS_herf,
                                          self.element.get_element_attribute_XPATH_herf)]):
                    key, val = self._get_text_or_attr(card, selectors[style][el_type], *funcs)
                    if key is not None:
                        new_element[key] = val
            new_element['scrape_time'] = scrape_time
            self.pipe.feed_items.append(new_element)
            self.pipe.num_of_elements_collected += 1
            self.timer.stop_timer()
            time_scraping_one_element = self.timer.get_elapsed_time()
            if self.pipe.num_of_elements_collected >= max_num_of_scraping:
                break

        df = pd.DataFrame(self.pipe.feed_items)
        df.to_csv("user_bio_data_scraped.csv", index=False)
        return len(self.pipe.feed_items),time_scraping_one_element




