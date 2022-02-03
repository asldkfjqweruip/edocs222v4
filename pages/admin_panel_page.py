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
        self.check_click(AdminPanelConstants.TASKTYPS)
        self.log.info("click create new case type")
        self.check_click(AdminPanelConstants.CREATETASKTYPS)
        self.log.info("fill required fields")
        self.fill_field(locator=AdminPanelConstants.TTFIELD, value=AdminPanelConstants.TEXT)
        self.log.info("save filled fields")
        self.check_click(AdminPanelConstants.BUTTONSAVE)
        self.log.info("reopen created cards")
        self.check_click(AdminPanelConstants.REOPENCRATED)
        self.log.info("send REQUIREDACTIONS reg")
        self.check_click(AdminPanelConstants.REQUIREDACTIONS)
        self.check_click(AdminPanelConstants.REGISTRATION)
        self.check_click(AdminPanelConstants.BUTTONSAVE)
        self.log.info("reopen created cards 2")
        sleep(1)
        self.check_click(AdminPanelConstants.REOPENCRATED)
        self.log.info("send REQUIREDACTIONS qr")
        self.check_click(AdminPanelConstants.REQUIREDACTIONS)
        self.check_click(AdminPanelConstants.QRCODE)
        self.check_click(AdminPanelConstants.BUTTONSAVE)
        self.log.info("wait error text")
        assert self.visibility_of_element_located(AdminPanelConstants.ERRORTEXT)
        self.log.info("fixing error")
        self.check_click(AdminPanelConstants.REQUIREDACTIONS)
        self.check_click(AdminPanelConstants.STAMPORSING)
        self.check_click(AdminPanelConstants.BUTTONSAVE)
        sleep(1)
        self.check_click(AdminPanelConstants.REOPENCRATED)
        self.log.info("deleting task type")
        self.check_click(AdminPanelConstants.DELETEFULL)
        assert self.element_is_not(AdminPanelConstants.REOPENCRATED)
