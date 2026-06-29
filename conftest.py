  
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver_utils import WebDriverUtils
from config.browser_config import BrowserConfig
from utils.logger import Logger
import os
from datetime import datetime
 
# Initialize logger
logger = Logger.setup_logger('ParaBank_Automation')
 
@pytest.fixture(scope="function")
def driver():
    """Setup and teardown WebDriver"""
    browser = BrowserConfig.get_browser()
    logger.info(f"Starting test with browser: {browser}")
    
    driver = WebDriverUtils.get_driver(browser)
    driver.get(BrowserConfig.get_url())
    
    yield driver
    
    driver.quit()
    logger.info("Browser closed")
 
@pytest.fixture(scope="function")
def wait(driver):
    """WebDriverWait fixture"""
    return WebDriverWait(driver, int(os.getenv('EXPLICIT_WAIT', 20)))
 
@pytest.fixture(scope="function")
def logger_fixture():
    """Logger fixture"""
    return logger
 
# Hook for browser selection via command line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="Browser to run tests on")
 
@pytest.fixture(scope="session")
def browser_choice(request):
    return request.config.getoption("--browser")
 
# Override driver fixture to use command line option
@pytest.fixture(scope="function")
def driver_with_browser_choice(browser_choice):
    """Driver with browser selection from command line"""
    browser = browser_choice or BrowserConfig.get_browser()
    driver = WebDriverUtils.get_driver(browser)
    driver.get(BrowserConfig.get_url())
    yield driver
    driver.quit()
 