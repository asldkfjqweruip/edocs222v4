# file
from constants.inside_doc_constants import InsideDocConstants
from constants.registry_constants import RegistryConstants
from pages.base_page import BasePage

# module
from time import sleep
import requests


class RegistryPage(BasePage):
    """"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = RegistryConstants

    def create_doc(self):
        """create doc"""
        self.log.info("go 2 registry documents")
        self.button_click(locator=RegistryConstants.DOCUMENTS)
        self.log.info("wait button")
        sleep(2)  # да каого! то он json то утек кудато
        self.log.info("click button +")
        self.button_click(locator=RegistryConstants.CREATEBUTTON)
        self.log.info("create doc")
        self.button_click(locator=RegistryConstants.CREATETSTDOC)
        assert self.visibility_of_element_located(value=InsideDocConstants.RIGHTSUCSESFUL)

        from pages.inside_doc_page import InsideDocPage
        return InsideDocPage(self.driver)

    def search_doc(self):
        """search doc"""
        self.log.info("go to registry document")
        self.button_click(locator=RegistryConstants.DOCUMENTS)
        sleep(1)
        self.log.info("flii search field")
        self.fill_field(locator=RegistryConstants.SEARCHBAR, value=self.constants.DOCFORSEARCH)
        self.log.info("start search")
        self.button_click(locator=RegistryConstants.SEARCHSTART)
        self.log.info("assert find search result")
        assert self.visibility_of_element_located(value=RegistryConstants.SEARCHRESULT)

    def add_assistant(self):
        self.button_click(locator=RegistryConstants.ASSISTANTREG)
        self.button_click(locator=RegistryConstants.ASSISTANTADDBUTTON)
        self.fill_field(locator=RegistryConstants.WHOASSIST, value='М. Ярмак')

    def go_to_admin(self):
        self.log.info("go to admin panel")
        self.button_click(RegistryConstants.ADMINBUTTON)
        from pages.admin_panel_page import AdminPanel
        return AdminPanel(self.driver)
