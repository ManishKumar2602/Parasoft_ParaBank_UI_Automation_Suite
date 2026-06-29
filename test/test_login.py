import pytest
from utils.excel_reader import ExcelReader
from pages.page_objects import LoginPage
import allure
 
@pytest.mark.regression
@pytest.mark.critical
class TestLogin:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait, logger_fixture):
        self.driver = driver
        self.wait = wait
        self.logger = logger_fixture
        self.login_page = LoginPage(driver, wait)
    
    @pytest.mark.parametrize("test_data",
        ExcelReader.read_test_data("login_data.xlsx"))
    def test_login_functionality(self, test_data):
        """Test login with different credentials"""
        
        self.logger.info(f"Executing test: {test_data['TestCaseID']}")
        self.logger.info(f"Testing with username: {test_data['Username']}")
        
        # Perform login
        self.login_page.login(test_data['Username'], test_data['Password'])
        
        # Verify result
        if test_data['ExpectedResult'] == 'success':
            assert self.login_page.is_login_successful(), "Login should be successful"
            self.logger.info("Login successful")
        else:
            error_msg = self.login_page.get_error_message()
            assert "error" in error_msg.lower() or "invalid" in error_msg.lower(), "Error message should be displayed"
            self.logger.info(f"Login failed as expected: {error_msg}")