# TikTok Scraper
![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas Badge](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Selenium Badge](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

A simple, efficient web scraper for TikTok that fetches data about videos, profiles, and hashtags.

## Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [File Descriptions](#file-descriptions)

## Installation

Before running the scraper, you need to install some Python packages. You can install them with the following command:

```bash
% pip install jupyter pandas numpy selenium selenium-wire pyobjc-framework-webkit webdriver-manager scipy scikit-learn statsmodels pmdarima
```

## Project Structure
```
tiktok_scraper/
├── __init__.py
├── main.py
│
├── spiders/
│   ├── __init__.py
│   ├── login_spider.py
│   ├── navigate_to_user_bio.py
│   └── search.py
│
├── page_objects/
│   ├── __init__.py
│   ├── get_feed_data.py
│   └── get_profile_bio_data.py
│
├── data_models/
│   ├── __init__.py
│   └── cleanning_data.py
│
├── pipelines/
│   ├── __init__.py
│   └── pipelines.py
│
├── middlewares/
│   ├── __init__.py
│   └── change_user_profiles.py
│
└── utils/
    ├── __init__.py
    ├── driver_manager.py
    └── scheduler.py
```


## File Descriptions

- `main.py`: The main script that runs your spider(s) and coordinates the other components. No classes are defined in this script, but it instantiates and uses classes from other modules. [main](main.py)

- `spiders/login_spider.py`: Contains the `LoginSpider` class, which navigates to the login page and logs in. [login_spider](spiders%2Flogin_spider.py)
- `spiders/navigate_to_user_bio.py`: Contains the `NavigateToUserBio` class, which navigates to the user bio page. [navigate_to_user_bio](spiders%2Fnavigate_to_user_bio.py)
- `spiders/search.py`: Contains the `Search` class, which navigates to the search page. [search](spiders%2Fsearch.py)

- `page_objects/get_feed_data.py`: Contains the `LoginPage` class, representing the login page and the interactions that can be performed on it. [get_feed_data](page_objects%2Fget_feed_data.py)
- `page_objects/get_profile_bio_data.py`: Contains the `ProfileBioPage` class, representing the profile bio page and the interactions that can be performed on it. [get_profile_bio_data](page_objects%2Fget_profile_bio_data.py)

- `data_models/cleanning_data.py`: Contains the `Product` class, representing a product and its associated data. [cleanning_data](data_models%2Fcleanning_data.py)

- `pipelines/pipeline.py`: Contains the `Pipeline` class, processing items returned by the spiders.[pipelines](pipelines%2Fpipelines.py)

- `middlewares/change_user_profiles.py`: Contains the `Middleware` class, providing hooks into certain stages of the scraping process.[change_user_profiles](middlewares%2Fchange_user_profiles.py)

- `utils/driver_manager.py`: Contains the `DriverManager` class, managing WebDriver instances. [driver_manager](utils%2Fdriver_manager.py)

- `utils/scheduler.py`: Contains the `Scheduler` class, scheduling and dispatching spiders. [scheduler](utils%2Fscheduler.py)
