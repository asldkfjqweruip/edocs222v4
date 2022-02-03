import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout=10)

    def fill_without_click(self, locator, value, by=By.XPATH):
        """Fill field"""
        field = self.wait_until_find_element(by=by, value=locator)
        field.send_keys(value)

    def fill_field(self, locator, value, by=By.XPATH):
        """Fill field"""
        field = self.wait_until_find_element(by=by, value=locator)
        field.click()
        field.clear()
        field.send_keys(value)

    def button_click(self, locator, by=By.XPATH):
        """Click button"""
        click = self.wait_until_find_element(by=by, value=locator)
        click.click()

    def check_click(self, value):
        self.wait_until_element_clickable(mark=value).click()




    def wait_until_find_element(self, value, by=By.XPATH):
        return self.wait.until(EC.presence_of_element_located(locator=(by, value)))

    def visibility_of_element_located(self, value, by=By.XPATH):
        return self.wait.until(EC.visibility_of_element_located(locator=(by, value)))

    def wait_until_element_clickable(self, mark):
        return self.wait.until(EC.element_to_be_clickable(mark))

    def element_is_not(self, value, by=By.XPATH):
        return self.wait.until_not(EC.presence_of_element_located(locator=(by, value)))
