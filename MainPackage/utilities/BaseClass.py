import inspect
import logging
import unittest
import allure
import pytest
from allure_commons.types import AttachmentType
from pathlib import Path

@pytest.mark.usefixtures("setup")
class BaseClass(unittest.TestCase):

    ROOT_PATH = str(Path(__file__).parent.parent)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def takeScreenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
