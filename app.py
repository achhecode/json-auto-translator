
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from logging_config import get_logger

logger = get_logger()

class App:
    def __init__(self):
        logger.info("App Operation Initiated")
        # Specify ChromeDriver path
        service = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=service)


    def start_chrome(self):
        driver.get("https://www.google.com")


