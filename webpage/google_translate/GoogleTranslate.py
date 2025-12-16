
from logging_config import get_logger
from helper.Common import *
from helper.JsonOperation import JsonOperation
import pyperclip
from impl.CustomSelenium import CustomSelenium
import time
from dotenv import load_dotenv
import os

load_dotenv()

logger = get_logger()

class GoogleTranslate:
    def __init__(self, driver):
        logger.info("Starting Operation On Google Translate Page!")
        self.driver = driver

        self.URL = "https://translate.google.com/"

        self.SL_LANGUAGE = os.getenv("SOURCE_LANGUAGE", "en")
        self.TL_LANGUAGE = os.getenv("TARGET_LANGUAGES", "ar,es,hi")

        # initialize objects

        FILE_PATH = os.getenv("FILE_PATH", f"./{self.SL_LANGUAGE}.json")
        self.OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER", "") # end with /

        
        self.json_ops_obj = JsonOperation(FILE_PATH)
        self.selenium_helper_obj = CustomSelenium(driver, default_timeout=10)
    

    def file_process(self):
        logger.info("Process file values for converting")
        return self.json_ops_obj.extract_unique_values()
        

    def start(self):
        all_unique_values = self.file_process()
        logger.info(all_unique_values)

        target_languages = [item.strip() for item in self.TL_LANGUAGE.split(",")]

        for lang in target_languages:
            URL = f"https://translate.google.co.in/?sl={self.SL_LANGUAGE}&tl={lang}&op=translate"

            self.driver.get(URL)
            translations = {}
            for value in all_unique_values:
                translations[value] = self.translate_text(value)

            self.json_ops_obj.replace_values_and_save(
                translation_map=translations,
                output_file=f"{self.OUTPUT_FOLDER}translations/{lang}.json"
            )
            self.wait(10)


    def select_languages(self):
        logger.info("Selecting languages")

        # click language dropdown
        # save_source(self.driver)
        # currently not required as language can be selected directly from url


    def translate_text(self, text_to_translate: str):
        # //textarea[@aria-label='Source text']

        # /html[1]/body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/c-wiz[1]/div[1]/div[7]/div[1]/div[1]
        # /html[1]/body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/c-wiz[1]/div[1]/div[7]/div[2]/div[1]
        
        try:
            # Step 1: Enter text into source field
            source_xpath = "//textarea[@aria-label='Source text']"
            if not self.selenium_helper_obj.input_text(source_xpath, text_to_translate):
                return None
            
            logger.info(f"Entered text: '{text_to_translate[:20]}...'")
            
            # Step 2: Wait for translation
            self.wait()
            
            # Step 3: Get translated text
            translation_xpath = "/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/c-wiz[1]/div[1]/div[6]/div[1]/div[1]"
            translated_text = self.selenium_helper_obj.get_text(translation_xpath, timeout=10)
            
            if translated_text:
                logger.info(f"Translation retrieved: '{translated_text[:50]}...'")
            else:
                logger.warning("No translation found")
                
            return translated_text
            
        except Exception as e:
            logger.error(f"Translation failed: {e}")
            return None


    def wait(self, tm=5):
        logger.info(f"Waiting {tm} seconds for translation...")
        time.sleep(tm)

            
    



