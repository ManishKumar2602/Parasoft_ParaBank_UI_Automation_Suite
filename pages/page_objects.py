from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
        # Locators
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@value='Log In']")
        self.error_message = (By.XPATH, "//p[@class='error']/preceding-sibling::h1")
        self.welcome_message = (By.XPATH, "//p[@class='smallText']")
    
    def login(self, username, password):
        self.wait.until(EC.element_to_be_clickable(self.username_input)).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    
    def get_error_message(self):
        return self.wait.until(EC.presence_of_element_located(self.error_message)).text
    
    def is_login_successful(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.welcome_message)).is_displayed()
        except:
            return False
 
class AccountServices:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
        # Common locators
        self.account_services_header = (By.XPATH, "//h1[contains(text(),'Account Services')]")
        
        # Account Services menu
        self.open_account_link = (By.XPATH, "//a[contains(text(),'Open New Account')]")
        self.accounts_overview_link = (By.XPATH, "//a[contains(text(),'Accounts Overview')]")
        self.transfer_funds_link = (By.XPATH, "//a[contains(text(),'Transfer Funds')]")
        self.bill_pay_link = (By.XPATH, "//a[contains(text(),'Bill Pay')]")
        self.find_transactions_link = (By.XPATH, "//a[contains(text(),'Find Transactions')]")
        self.update_contact_info_link = (By.XPATH, "//a[contains(text(),'Update Contact Info')]")
        self.request_loan_link = (By.XPATH, "//a[contains(text(),'Request Loan')]")
        self.logout_link = (By.XPATH, "//a[contains(text(),'Log Out')]")
 
class OpenAccountPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
        self.account_type_dropdown = (By.ID, "type")
        self.account_from_dropdown = (By.ID, "fromAccountId")
        self.open_account_button = (By.XPATH, "//input[@value='Open New Account']")
        self.success_message = (By.XPATH, "//p[contains(text(),'Congratulations')]")
        self.account_id = (By.XPATH, "//a[contains(@href, 'activity.htm')]")
    
    def open_new_account(self, account_type="CHECKING", from_account_id="14565"):
        Select(self.wait.until(EC.element_to_be_clickable(self.account_type_dropdown))).select_by_visible_text(account_type)
        Select(self.driver.find_element(*self.account_from_dropdown)).select_by_value(from_account_id)
        self.driver.find_element(*self.open_account_button).click()
    
    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_message)).text
    
    def get_new_account_id(self):
        return self.wait.until(EC.presence_of_element_located(self.account_id)).text
 
class TransferFundsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
        self.amount_input = (By.ID, "amount")
        self.from_account_dropdown = (By.ID, "fromAccountId")
        self.to_account_dropdown = (By.ID, "toAccountId")
        self.transfer_button = (By.XPATH, "//input[@value='Transfer']")
        self.success_message = (By.XPATH, "//h1[contains(text(),'Transfer Complete!')]")
        self.error_message = (By.XPATH, "//p[@class='error']")
    
    def transfer_funds(self, amount, from_account_id="13566", to_account_id="13566"):
        self.wait.until(EC.element_to_be_clickable(self.amount_input)).send_keys(amount)
        Select(self.driver.find_element(*self.from_account_dropdown)).select_by_value(from_account_id)
        Select(self.driver.find_element(*self.to_account_dropdown)).select_by_value(to_account_id)
        self.driver.find_element(*self.transfer_button).click()
    
    def is_transfer_successful(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.success_message)).is_displayed()
        except:
            return False
    
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text
 
class RequestLoanPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
        self.loan_amount_input = (By.ID, "amount")
        self.down_payment_input = (By.ID, "downPayment")
        self.from_account_dropdown = (By.ID, "fromAccountId")
        self.apply_now_button = (By.XPATH, "//input[@value='Apply Now']")
        self.success_message = (By.XPATH, "//p[contains(text(),'Congratulations')]")
        self.denial_message = (By.XPATH, "//p[contains(text(),'We cannot grant a loan')]")
    
    def apply_loan(self, amount, down_payment, from_account_id="13566"):
        self.wait.until(EC.element_to_be_clickable(self.loan_amount_input)).send_keys(amount)
        self.driver.find_element(*self.down_payment_input).send_keys(down_payment)
        Select(self.driver.find_element(*self.from_account_dropdown)).select_by_value(from_account_id)
        self.driver.find_element(*self.apply_now_button).click()
    
    def is_loan_approved(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.success_message)).is_displayed()
        except:
            return False