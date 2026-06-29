import pytest
from pages.page_objects import LoginPage, AccountServices, OpenAccountPage
import allure
 
@pytest.mark.regression
class TestOpenAccount:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait, logger_fixture):
        self.driver = driver
        self.wait = wait
        self.logger = logger_fixture
        self.login_page = LoginPage(driver, wait)
        self.account_services = AccountServices(driver, wait)
        self.open_account_page = OpenAccountPage(driver, wait)
        
        # Login first
        self.login_page.login("john", "demo")
        assert self.login_page.is_login_successful(), "Login should be successful"
    
    def test_open_new_checking_account(self):
        """Test opening a new checking account"""
        
        # Navigate to Open New Account
        self.driver.find_element(*self.account_services.open_account_link).click()
        self.logger.info("Navigated to Open New Account")
        
        # Open new checking account
        self.open_account_page.open_new_account("CHECKING", "13344")
        self.logger.info("Opened new checking account")
        
        # Verify success
        success_msg = self.open_account_page.get_success_message()
        print(f"✅Success message: {success_msg}")
        assert "Congratulations" in success_msg, "Account opening should be successful"
        
        new_account_id = self.open_account_page.get_new_account_id()
        assert new_account_id.isdigit(), "New account ID should be numeric"
        self.logger.info(f"New account created with ID: {new_account_id}")