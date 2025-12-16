from loguru import logger
from logging_config import get_logger


logger = get_logger()

def main():
    logger.debug("That's it, beautiful and simple logging!")
    logger.info("Application started")
    logger.debug("Debug message")



if __name__ == "__main__":
    main()