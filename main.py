from loguru import logger
from logging_config import get_logger
from app import App

logger = get_logger()

def main():
    logger.debug("That's it, beautiful and simple logging!")
    logger.info("Application started")
    logger.debug("Debug message")
    self.app_obj = App()
    self.app_obj.start_chrome()



if __name__ == "__main__":
    main()