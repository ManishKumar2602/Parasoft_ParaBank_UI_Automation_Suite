import pytest
from pages.page_objects import LoginPage, AccountServices
from utils.excel_reader import ExcelReader
import allure
import time
 
@pytest.mark.regression
class TestLogout:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait, logger_fixture):
        self.driver = driver
        self.wait = wait
        self.logger = logger_fixture
        self.login_page = LoginPage(driver, wait)
        self.account_services = AccountServices(driver, wait)
    
    def test_logout_functionality(self):
        """Test logout functionality"""
        
        # Login first
        self.login_page.login("john", "demo")
        assert self.login_page.is_login_successful(), "Login should be successful"
        self.logger.info("Logged in successfully")
        
        # Click logout
        self.driver.find_element(*self.account_services.logout_link).click()
        time.sleep(1)  # Wait for logout to complete
        self.logger.info("Clicked logout")
        
        # Verify logout - check if login form appears
        assert "Log In" in self.driver.page_source, "Login form should be displayed"
        # assert "Welcome" not in self.driver.page_source, "Welcome message should not be displayed"
        self.logger.info("Logout successful")