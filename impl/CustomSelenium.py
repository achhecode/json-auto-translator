import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging_config import get_logger

logger = get_logger()

class CustomSelenium:
    def __init__(self, driver, default_timeout: int = 5):
        self.driver = driver
        self.default_timeout = default_timeout

    def input_text(self, xpath: str, text: str, timeout: int = None):
        """
        Enter text into an input field using XPath
        
        Args:
            xpath: XPath selector for the element
            text: Text to enter
            timeout: Optional custom timeout (uses default if None)
        """
        try:
            wait = WebDriverWait(self.driver, timeout or self.default_timeout)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            
            # Clear existing text if any
            element.clear()
            # Enter text
            element.send_keys(text)
            
            logger.info(f"Entered text into element: {xpath}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to input text: {e}")
            return False

    def get_text(self, xpath: str, timeout: int = None):
        """
        Get text from an element using XPath
        
        Args:
            xpath: XPath selector for the element
            timeout: Optional custom timeout
            
        Returns:
            Text content or None if failed
        """
        try:
            wait = WebDriverWait(self.driver, timeout or self.default_timeout)
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            
            text = element.text
            logger.info(f"Retrieved text from element: {xpath}")
            return text
            
        except Exception as e:
            logger.error(f"Failed to get text: {e}")
            return None

    
