import logging
import pytest

# file
from constants.credential import Credential
from pages.login_page import LoginPage
from pages.utilities import create_driver


@pytest.mark.parametrize('browser', [Credential.CHROME, Credential.FIREFOX])
class TestMain:

    @pytest.fixture(scope="function")
    def log(self):
        """logs"""
        log = logging.getLogger()
        yield log

    @pytest.fixture(scope="function")
    def driver(self, browser):
        """webdriver manager parametrize"""
        driver = create_driver(browser)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def prepare_page(self, driver):
        """pre-condition
            - driver get url
            - login
            - send driver to page"""
        driver.get(Credential.URLPROD)
        yield LoginPage(driver).login(Credential.PRODTENANCY, Credential.LOGIN, Credential.PASSWORD)

    def test_create_doc(self, prepare_page):
        """create doc"""
        registry_page = prepare_page
        registry_page.create_doc()

    def test_doc_search(self, prepare_page):
        """search doc"""
        search_doc = prepare_page
        search_doc.search_doc()

    def test_add_assistant(self, prepare_page):
        """add assistant"""
        add_assistant = prepare_page
        add_assistant.add_assistant()
