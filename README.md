Parasoft_ParaBank_UI_Automation_Suite/
├── config/
│   ├── __init__.py
│   └── browser_config.py
├── fixtures/
│   ├── __init__.py
│   └── webdriver_fixtures.py
├── logs/
│   └── (log files will be generated here)
├── reports/
│   └── (test reports will be generated here)
├── test/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_open_account.py
│   ├── test_transfer_funds.py
│   └── test_request_loan.py
├── test_data/
│   ├── __init__.py
│   ├── login_data.xlsx
│   └── test_data_loader.py
├── utils/
│   ├── __init__.py
│   ├── excel_reader.py
│   ├── logger.py
│   └── webdriver_utils.py
├── venv/
├── .env
├── .gitignore
├── conftest.py
├── pytest.ini
└── requirements.txt


Running Tests
Run all tests with default browser (from .env)
bash
pytest
Run specific browser
bash
pytest --browser=firefox
pytest --browser=edge
pytest --browser=safari
Run specific test file
bash
pytest test/test_login.py
Run tests with markers
bash
pytest -m regression
pytest -m critical
Run tests in parallel
bash
pytest -n 4
Generate Allure report
bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
Run with html report
bash
pytest --html=reports/report.html
Rerun failed tests
bash
pytest --reruns 3
