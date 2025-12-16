
from logging_config import get_logger

logger = get_logger()

class GoogleTranslate:
    def __init__(self, driver):
        logger.info("Starting Operation On Google Translate Page!")
        self.driver = driver
        self.URL = "https://translate.google.co.in/?sl=auto&tl=en&op=translate"

    def start(self):
        self.driver.get(self.URL)
        self.select_languages()


    def select_languages(self, lang_from, lang_to):
        logger.info("Selecting languages")


