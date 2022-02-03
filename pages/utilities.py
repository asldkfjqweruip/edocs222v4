import datetime
import logging
from time import sleep
# driver elements
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as options_chrome
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as ServiceF
from selenium.webdriver.firefox import options as options_firefox
# file
from constants.credential import Credential



def create_driver(browser):
    if browser == Credential.CHROME:
        options = options_chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
    elif browser == Credential.FIREFOX:
        options = options_firefox
        service = ServiceF(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.implicitly_wait(10)
    else:
        raise AttributeError(f"unknown browser name {browser}")
    return driver



def log_decorator(orig_func):
    """log based on docstring"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecor]")
        log.info("%s. :params: (args: %s; kwargs: %s))", orig_func.__doc__, str(args), str(kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


# круто, провозился пару часов но element is not attached to the page document! он не решает :/
def wait_until_ok_decorator(timeout=10, period=1):
    log = logging.getLogger("[Wait until ok decorator started]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.warning(f"i Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator
