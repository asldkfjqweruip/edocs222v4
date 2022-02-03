import logging
import pytest

# file
from constants.credential import Credential
from pages.login_page import LoginPage
from pages.utilities import create_driver


@pytest.mark.parametrize('browser', [Credential.CHROME, Credential.FIREFOX])
class TestAdminPanel:

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
    def prepare_page(self, driver):
        """pre-condition
            - driver get url
            - send driver to page"""
        driver.get(Credential.URLPROD)
        # Credential . tenancy , login , password
        yield LoginPage(driver).login(Credential.PRODTENANCY, Credential.LOGIN, Credential.PASSWORD)

    def test_admin(self, prepare_page):
        """Pre-condition
            - logined driver go to admin panel
        Test steps
            - open task type
            - click create new case type
            - fill task type name and save
            - reopen created task type, add required actions, save card
            - reopen created task type, add forbidden actions combination try save
            - validate presence  error, fix error
            - reopen card delete created task type
            - validate created task type is deleted"""
        admin_panel = prepare_page.go_to_admin()
        admin_panel.task_type()
