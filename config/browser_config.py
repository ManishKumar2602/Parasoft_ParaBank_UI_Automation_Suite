import os
from dotenv import load_dotenv
 
load_dotenv()
 
class BrowserConfig:
    @staticmethod
    def get_browser():
        """Get browser from command line or .env file"""
        # Check command line argument first
        import sys
        for arg in sys.argv:
            if arg.startswith('--browser='):
                browser = arg.split('=')[1]
                return browser.lower()
        
        # Fall back to .env
        return os.getenv('BROWSER', 'chrome').lower()
    
    @staticmethod
    def get_url():
        return os.getenv('BASE_URL', 'https://parabank.parasoft.com/parabank/index.htm')