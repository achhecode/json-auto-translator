from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from logging_config import get_logger

logger = get_logger()

class ChromeManager:
    def __init__(self, headless=False):
        """
        Initialize Chrome with efficient settings
        
        Args:
            headless: Run browser in background (no GUI)
        """
        logger.info("Initializing Chrome Manager")
        
        # Configure Chrome for efficiency
        chrome_options = Options()
        
        if headless:
            chrome_options.add_argument("--headless")
        
        # Efficiency optimizations
        chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        chrome_options.add_argument("--disable-extensions")  # Disable extensions
        chrome_options.add_argument("--disable-notifications")  # Disable notifications
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Performance settings
        prefs = {
            'profile.default_content_setting_values.notifications': 2,  # Block notifications
            'credentials_enable_service': False,  # Disable password saving
            'profile.password_manager_enabled': False,
            'profile.default_content_settings.popups': 0,  # Block popups
        }
        chrome_options.add_experimental_option('prefs', prefs)
        
        # Load driver
        service = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Set timeouts for efficiency
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(5)
        
    def open_url(self, url="https://www.google.com"):
        """Open a URL and return control immediately"""
        try:
            logger.info(f"Opening URL: {url}")
            self.driver.get(url)
            return True
        except Exception as e:
            logger.error(f"Failed to open URL: {e}")
            return False
    
    def keep_open_lightweight(self):
        """
        Keep browser open with minimal CPU usage
        - Browser stays open but script doesn't consume CPU
        - Easy to close with keyboard shortcut
        """
        print("\n" + "="*60)
        print("CHROME IS NOW RUNNING")
        print("="*60)
        print("\nACTIVE BROWSER CONTROLS:")
        print("-" * 40)
        print("Browser Window:    Open for manual interaction")
        print("Close Browser:     Click the 'X' button or Alt+F4")
        print("Python Script:     Already idle (minimal CPU usage)")
        print("-" * 40)
        print("\nScript is now in low-power waiting mode...")
        print("Press 'Ctrl+C' in terminal to completely exit.\n")
        
        try:
            # Minimal CPU usage - just check if browser is alive occasionally
            while True:
                try:
                    # This check is very lightweight
                    _ = self.driver.title
                    time.sleep(10)  # Check every 10 seconds (very low CPU)
                except:
                    logger.info("Browser closed by user")
                    break
                    
        except KeyboardInterrupt:
            print("\n" + "="*60)
            print("EXITING PROGRAM")
            print("="*60)
            print("\nNote: Close Chrome window manually if still open.")
    
    def close_all(self):
        """Cleanly close everything"""
        try:
            self.driver.quit()
            logger.info("Browser closed")
        except:
            pass
        print("\nProgram terminated cleanly.")
