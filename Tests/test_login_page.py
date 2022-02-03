import logging
import pytest

# file
from constants.credential import Credential
from pages.login_page import LoginPage
from pages.utilities import create_driver

@pytest.mark.parametrize('browser', [Credential.CHROME, Credential.FIREFOX])
class TestLogin:

    @pytest.fixture(scope="function")
    def log(self):
        """logs"""
        log = logging.getLogger()
        yield log

    @pytest.fixture(scope="function")
    def driver(self, browser):
        """webdriver manager"""
        driver = create_driver(browser)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def login_page(self, driver):
        """pre-condition
            - driver get url
            - send driver to page"""
        driver.get(Credential.URLPROD)

        return LoginPage(driver)

    def test_login(self, login_page):
        """login - expected login and password"""
        login_page.login(Credential.PRODTENANCY, Credential.LOGIN, Credential.PASSWORD)



