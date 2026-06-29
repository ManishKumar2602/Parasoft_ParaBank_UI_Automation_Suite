import pytest
from pages.page_objects import LoginPage, AccountServices, TransferFundsPage
import allure
 
@pytest.mark.regression
class TestTransferFunds:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait, logger_fixture):
        self.driver = driver
        self.wait = wait
        self.logger = logger_fixture
        self.login_page = LoginPage(driver, wait)
        self.account_services = AccountServices(driver, wait)
        self.transfer_page = TransferFundsPage(driver, wait)
        
        # Login first
        self.login_page.login("john", "demo")
        assert self.login_page.is_login_successful(), "Login should be successful"
    
    def test_transfer_funds(self):
        """Test transferring funds between accounts"""
        
        # Navigate to Transfer Funds
        self.driver.find_element(*self.account_services.transfer_funds_link).click()
        self.logger.info("Navigated to Transfer Funds")
        
        # Transfer funds
        self.transfer_page.transfer_funds("100", "13677", "13899")
        self.logger.info("Transferred $100")
        
        # Verify success
        assert self.transfer_page.is_transfer_successful(), "Transfer should be successful"
        self.logger.info("Transfer completed successfully")
    @pytest.mark.xfail(reason="Open issue with insufficient funds error handling")
    def test_transfer_with_insufficient_funds(self):
        """Test transfer with insufficient funds"""
        
        # Navigate to Transfer Funds
        self.driver.find_element(*self.account_services.transfer_funds_link).click()
        
        # Try to transfer more than available
        self.transfer_page.transfer_funds("999999", "13677", "13899")
        
        # Verify error
        error_msg = self.transfer_page.get_error_message()
        assert "insufficient" in error_msg.lower(), "Error message should indicate insufficient funds"
        self.logger.info("Insufficient funds error handled correctly")