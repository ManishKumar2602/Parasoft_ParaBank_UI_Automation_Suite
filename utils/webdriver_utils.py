from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
 
class WebDriverUtils:
    @staticmethod
    def get_driver(browser_name):
        """Create and return WebDriver instance based on browser name"""
        
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-notifications')
            options.add_argument('--start-maximized')
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
        
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--start-maximized')
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
        
        elif browser_name == 'edge':
            options = webdriver.EdgeOptions()
            options.add_argument('--start-maximized')
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )
        
        elif browser_name == 'safari':
            driver = webdriver.Safari()
            driver.maximize_window()
        
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        # Set timeouts
        driver.implicitly_wait(int(os.getenv('IMPICIT_WAIT', 10)))
        driver.set_page_load_timeout(int(os.getenv('PAGE_LOAD_TIMEOUT', 30)))
        
        return driver