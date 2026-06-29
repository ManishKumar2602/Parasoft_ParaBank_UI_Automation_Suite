import pytest
from pages.page_objects import LoginPage, AccountServices, RequestLoanPage
import allure
 
@pytest.mark.regression
class TestRequestLoan:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait, logger_fixture):
        self.driver = driver
        self.wait = wait
        self.logger = logger_fixture
        self.login_page = LoginPage(driver, wait)
        self.account_services = AccountServices(driver, wait)
        self.loan_page = RequestLoanPage(driver, wait)
        
        # Login first
        self.login_page.login("john", "demo")
        assert self.login_page.is_login_successful(), "Login should be successful"
    
    def test_request_small_loan(self):
        """Test requesting a small loan that should be approved"""
        
        # Navigate to Request Loan
        self.driver.find_element(*self.account_services.request_loan_link).click()
        self.logger.info("Navigated to Request Loan")
        
        # Apply for loan
        self.loan_page.apply_loan("1000", "100", "13344")
        self.logger.info("Applied for $1000 loan")
        
        # Verify approval
        assert self.loan_page.is_loan_approved(), "Loan should be approved"
        self.logger.info("Loan approved successfully")
    
    def test_request_large_loan(self):
        """Test requesting a large loan that should be denied"""
        
        # Navigate to Request Loan
        self.driver.find_element(*self.account_services.request_loan_link).click()
        
        # Apply for large loan
        self.loan_page.apply_loan("100000", "1000", "13344")
        self.logger.info("Applied for $100000 loan")
        
        # Verify denial
        assert not self.loan_page.is_loan_approved(), "Large loan should be denied"
        self.logger.info("Large loan denied as expected")