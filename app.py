
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from logging_config import get_logger
from ChromeManager import ChromeManager


logger = get_logger()

class App:
    def __init__(self):
        logger.info("App Operation Initiated")
        

    def start_chrome(self):
        chrome = ChromeManager(headless=False)
        chrome.open_url("https://www.google.com")
        chrome.keep_open_lightweight()
        chrome.close_all()


