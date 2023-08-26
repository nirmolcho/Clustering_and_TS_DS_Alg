# Final Project - Principles and Technologies for Data Science

![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas Badge](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn Badge](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logoColor=white)
![Scikit-learn Badge](https://img.shields.io/badge/Scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly Badge](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)
![Selenium Badge](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Jupyter Badge](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![PyCharm Badge](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)
![yfinance Badge](https://img.shields.io/badge/yfinance-000000?style=for-the-badge&logo=yahoo&logoColor=white)
![ergast Badge](https://img.shields.io/badge/ergast-000000?style=for-the-badge&logo=ergast&logoColor=white)
---

This is the final project for our Principles and Technologies for Data Science course. 

We have chosen to work on "F1" data from the [Ergast Developer API](https://ergast.com/mrd/).

And we used yfinance to get the stock data [yfinance API](https://pypi.org/project/yfinance/).

---

## Installation
To run this project, make sure to install the following libraries:

```bash
pip install jupyter pandas numpy selenium selenium-wire pyobjc-framework-webkit webdriver-manager scipy scikit-learn statsmodels pmdarima yfinance plotly
```

## Directory Structure

The project is organized into several directories, each with its unique purpose:

- **Scraping**: This directory contains the core functionality of our scraper. It includes the main function for running the scraper and the Selenium commands used for scraping, plus using an API to get all the data from the website.

- **EDA and Data Cleaning**: This is where we perform exploratory data analysis and clean our scraped data. It houses all the scripts and notebooks used in these data preprocessing steps.

- **Clustering**: In this directory, we apply different clustering techniques to our data. Here, you'll find our implementation of various sequences and three distinct clustering methods.

- **Time Series Prediction**: Our time series prediction models are contained in this directory. We have implemented three different types of time series predictions here: ARIMA, GRACH, Wavelet Analysis and SVM models.

- **task requirements**: This directory contains the requirements for the project. [task requirements](requirements.md)




