import time
from datetime import timedelta, datetime


class Timer:
    def __init__(self):
        self.start = None
        self.end = None
        self.time = None

    def start_timer(self):
        self.start = time.time()

    def end_timer(self):
        self.end = time.time()
        self.time = str(timedelta(seconds=int(self.end - self.start)))


class Config:
    def __init__(self):
        self.max_elements = 50
        self.time_sleep = 4
        self.time_sleep_for_profile = 2
        self.user_name = "just4tester22@gmail.com"
        self.password = "Pa##w0rd"

        self.tweet_data = []
        self.user_bio_data = []
        self.tweet_count = 0
        self.user_urls = set()
        self.visited_urls = set()

# Usage


