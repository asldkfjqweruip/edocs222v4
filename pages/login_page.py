from time import sleep

from pages.base_page import BasePage
from constants.login_constants import LoginConstants
from constants.registry_constants import RegistryConstants


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = LoginConstants

    def login(self, tenancy, login_value, password_value):
        """login
        - fill tenancy
        - fill login
        - fill password
        - click stay un
        - choose user from list """

        self.log.info("fill tenancy")
        self.fill_field(locator=self.constants.TENANCYNAME, value=tenancy)
        self.button_click(locator=self.constants.TENANCYENTERBUTTON)
        self.log.info("fill login")
        self.fill_field(locator=self.constants.LOGINFIELD, value=login_value)
        self.button_click(locator=self.constants.NEXTTOPASSWORDBUTON)
        self.log.info("fill password")
        # element is not attached to the page document!
        # or StaleElementReferenceException
        try:
            self.fill_field(locator=self.constants.PASWORDFIELD, value=password_value)
            self.button_click(locator=self.constants.LOGINBUTTON)
        except Exception:
            self.log.info("Exception happens")
            sleep(1)
            self.fill_field(locator=self.constants.PASWORDFIELD, value=password_value)
            self.button_click(locator=self.constants.LOGINBUTTON)
        self.log.info("stay in click")
        self.button_click(locator=self.constants.STAYINBUTTON)
        self.log.info("choose user from list")
        # TODO: дополнить! если пользователь один то данной формы нет!
        #  (хотя и у тестовых пользователей всегда много учеток)
        self.button_click(locator=self.constants.USERCHOISE)
        self.log.info("verify element from Registry")
        assert self.wait_until_find_element(value=RegistryConstants.DOCUMENTS)
        self.log.info("resend driver condition to RegistryPage")
        from pages.registry_page import RegistryPage
        return RegistryPage(self.driver)
