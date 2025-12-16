
from logging_config import get_logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webpage.google_translate.GoogleTranslate import GoogleTranslate

logger = get_logger()

class App:
    def __init__(self):
        logger.info("App Operation Initiated")
        # 1. Setup options
        options = Options()
        options.add_experimental_option("detach", True)  # Browser stays open

        # 2. Create driver
        service = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=service, options=options)

        # Starting operation for Google Translate Page
        GoogleTranslate(self.driver).start()
