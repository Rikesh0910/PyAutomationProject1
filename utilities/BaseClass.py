import inspect

import pytest
import logging

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("logfile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(format)
        if(logger.hasHandlers()):
            logger.handlers.clear()
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def handle_alert(self):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            self.driver.switch_to.default_content()
        except NoAlertPresentException:
            print("No alert present")

    def explicit_wait(self, text):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, text)))


