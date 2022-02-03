from constants.admin_panel_constants import AdminPanelConstants
from pages.base_page import BasePage
from time import sleep


class AdminPanel(BasePage):
    """"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = AdminPanelConstants

    def task_type(self):
        """task type create, update , delete"""
        self.log.info("open register task type")
        sleep(1)
        self.button_click(AdminPanelConstants.TASKTYPS)
        self.log.info("click create new case type")
        sleep(1)
        self.button_click(AdminPanelConstants.CREATETASKTYPS)
        self.log.info("fill required fields")
        sleep(1)
        self.fill_field(locator=AdminPanelConstants.TTFIELD, value=AdminPanelConstants.TEXT)
        self.log.info("save filled fields")
        sleep(1)
        self.button_click(AdminPanelConstants.BUTTONSAVE)
        self.log.info("reopen created cards")
        sleep(1)
        self.button_click(AdminPanelConstants.REOPENCRATED)
        self.log.info("send REQUIREDACTIONS reg")
        sleep(1)
        self.button_click(AdminPanelConstants.REQUIREDACTIONS)
        sleep(1)
        self.button_click(AdminPanelConstants.REGISTRATION)
        sleep(1)
        self.button_click(AdminPanelConstants.BUTTONSAVE)
        self.log.info("reopen created cards 2")
        sleep(2)
        self.button_click(AdminPanelConstants.REOPENCRATED)
        self.log.info("send REQUIREDACTIONS qr")
        sleep(1)
        self.button_click(AdminPanelConstants.REQUIREDACTIONS)
        sleep(1)
        self.button_click(AdminPanelConstants.QRCODE)
        sleep(1)
        self.button_click(AdminPanelConstants.BUTTONSAVE)
        self.log.info("wait error text")
        sleep(1)
        assert self.visibility_of_element_located(AdminPanelConstants.ERRORTEXT)
        self.log.info("fixing error")
        sleep(1)
        self.button_click(AdminPanelConstants.REQUIREDACTIONS)
        sleep(1)
        self.button_click(AdminPanelConstants.STAMPORSING)
        sleep(1)
        self.button_click(AdminPanelConstants.BUTTONSAVE)
        sleep(2)
        self.button_click(AdminPanelConstants.REOPENCRATED)
        self.log.info("deleting task type")
        sleep(1)
        self.button_click(AdminPanelConstants.DELETEFULL)
        sleep(1)
        assert self.element_is_not(AdminPanelConstants.REOPENCRATED)
