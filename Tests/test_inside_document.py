import logging
import pytest

# file
from constants.credential import Credential
from pages.login_page import LoginPage
from pages.utilities import create_driver


@pytest.mark.parametrize('browser', [Credential.CHROME, Credential.FIREFOX])
class TestInsideDocument:

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
        yield LoginPage(driver).login(Credential.PRODTENANCY, Credential.LOGIN, Credential.PASSWORD)

    def test_doc_registration(self, prepare_page):
        insidedocpage = prepare_page.create_doc()
        insidedocpage.registry()

    def test_doc_executed(self, prepare_page):
        route_executed = prepare_page.create_doc()
        route_executed.route()

    # def test_fill_card_field(self, prepare_page):
    #     insidedocpage = prepare_page.create_doc()
    #     insidedocpage.fil_some_field()
