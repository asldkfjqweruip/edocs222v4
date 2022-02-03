from constants.inside_doc_constants import InsideDocConstants
from pages.base_page import BasePage

from datetime import datetime

from time import sleep


class InsideDocPage(BasePage):
    """"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = InsideDocConstants

    def registry(self):
        """registry doc"""
        self.log.info("wait until rights validate")
        self.wait_until_find_element(value=InsideDocConstants.RIGHTSUCSESFUL)
        self.log.info("create original doc-title string")
        before = self.wait_until_find_element(value=InsideDocConstants.DOCTITLE).get_attribute("Title")
        self.log.info(f"doc title before now {before}")
        self.log.info("open registration block")
        self.button_click(locator=InsideDocConstants.REGISTRATIONOPEN)
        self.log.info("execute registration")
        self.button_click(locator=InsideDocConstants.REGISTRATIONEXECUTE)
        sleep(2)  # waiter 2 reload title
        after = self.wait_until_find_element(value=InsideDocConstants.DOCTITLE).get_attribute("Title")
        self.log.info(f"doc title after now = {after}")
        assert before != after

    def route(self):
        """execute document"""
        self.log.info("send to route")
        self.button_click(locator=InsideDocConstants.SENDTOROUTE)
        self.log.info("send without reg")
        self.button_click(locator=InsideDocConstants.SENDWITHOUTREG)
        self.log.info("wait until finde")
        sleep(5)
        self.button_click(locator=InsideDocConstants.ROUTEEXECUTE)
        self.button_click(locator=InsideDocConstants.EXECUTEDOCUMENT)
        self.button_click(locator=InsideDocConstants.ROUTEEXECUTEANYWAY)
        indoc = self.driver.current_url
        self.log.info(f"{indoc}")
        sleep(5)
        out = self.driver.current_url
        self.log.info((f"{out}"))
        assert indoc != out

    # TODO : Work in progress
    def addcommentary(self):
        self.button_click(locator=InsideDocConstants.COMMENTARY)
        self.fill_field(locator=InsideDocConstants.COMMENTARYFIELD, value=datetime.now())

    def fil_some_field(self):
        self.button_click(locator=InsideDocConstants.SHORTTEXTFIELD)
        self.fill_field(locator=InsideDocConstants.SHORTTEXTV2, value='aporuhgpqaorehgpoqaher')
        self.fill_without_click(locator=InsideDocConstants.SHORTTEXTV2, value='aporuhgpqaorehgpoqaher')



