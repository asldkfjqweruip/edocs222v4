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
        self.button_click(AdminPanelConstants.TASKTYPS)
        self.log.info("click create new case type")
        self.button_click(AdminPanelConstants.CREATETASKTYPS)
        self.log.info("fill required fields")
        self.fill_field(locator=AdminPanelConstants.TTFIELD, value=AdminPanelConstants.TEXT)
        self.log.info("save filled fields")
        self.button_click(AdminPanelConstants.BUTTONSAVE)
        self.log.info("reopen created cards")
        self.button_click(AdminPanelConstants.REOPENCRATED)
        self.log.info("send REQUIREDACTIONS reg")
        self.button_click(AdminPanelConstants.REQUIREDACTIONS)
        self.button_click(AdminPanelConstants.REGISTRATION)
        self.button_click(AdminPanelConstants.BUTTONSAVE)
        self.log.info("reopen created cards 2")
        sleep(1)
        self.button_click(AdminPanelConstants.REOPENCRATED)
        self.log.info("send REQUIREDACTIONS qr")
        self.button_click(AdminPanelConstants.REQUIREDACTIONS)
        self.button_click(AdminPanelConstants.QRCODE)
        self.button_click(AdminPanelConstants.BUTTONSAVE)
        self.log.info("wait error text")
        assert self.visibility_of_element_located(AdminPanelConstants.ERRORTEXT)
        self.log.info("fixing error")
        self.button_click(AdminPanelConstants.REQUIREDACTIONS)
        self.button_click(AdminPanelConstants.STAMPORSING)
        self.button_click(AdminPanelConstants.BUTTONSAVE)
        sleep(1)
        self.button_click(AdminPanelConstants.REOPENCRATED)
        self.log.info("deleting task type")
        self.button_click(AdminPanelConstants.DELETEFULL)
        assert self.element_is_not(AdminPanelConstants.REOPENCRATED)
