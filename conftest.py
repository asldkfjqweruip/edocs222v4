import logging
import os

from constants.credential import Credential


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)


# 17Й 1:20
#def pytest_sessionstart(session):
    #os.environ["PATH"] = os.environ["PATH"] + f":{os.path.abspath(Credential.DRIVERSPATH)}"
