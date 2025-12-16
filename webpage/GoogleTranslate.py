
from logging_config import get_logger
from helper.Common import *
from helper.JsonOperation import JsonOperation
import pyperclip

logger = get_logger()

class GoogleTranslate:
    def __init__(self, driver, file_path):
        logger.info("Starting Operation On Google Translate Page!")
        self.driver = driver
        self.file_path = file_path

        self.URL = "https://translate.google.com/"

        sl_language = "en"
        to_language = "ar"

        self.URL = f"https://translate.google.co.in/?sl={sl_language}&tl={to_language}&op=translate"

        # initialize objects
        self.json_ops = JsonOperation("./en.json")

    def file_process(self):
        logger.info("Process file values for converting")
        return self.json_ops.extract_unique_values()
        

    def start(self):
        all_unique_values = self.file_process()
        logger.info(all_unique_values)
        self.driver.get(self.URL)
        translations = {}
        for value in all_unique_values:
            translations[value] = "4.1.3 ¿Cómo estás?"

        self.json_ops.replace_values_and_save(
            translation_map=translations,
            output_file="output_es.json"
        )
        # self.select_languages()


    def select_languages(self):
        logger.info("Selecting languages")

        # click language dropdown
        # save_source(self.driver)
        # currently not required as language can be selected directly from url

    



