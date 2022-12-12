import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from helpers.selenium_helper import initialize_chrome_webdriver, type_text


class VRM:
    """
    User actions for MyDay.me web application
    """

    def __init__(self) -> None:
        """
        Initialize the Chrome driver
        """
        self.driver = initialize_chrome_webdriver()

    def load_app(self):
        """
        Navigate to the VRM demo web application
        """
        self.driver.get("https://vrm.victronenergy.com")
        time.sleep(3)

    def navigate_to_device_list(self):
        """
        Navigate to the device list
        """
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/section[1]/div/div/div/div[3]/div[3]/div/a[1]").click()
        time.sleep(3)

    def get_installation_by_id(self, device_id: str):
        """
        Get an installation by inputting the id of the installation
        Args:
            device_id: str (unique)
        """
        self.driver.get(f"https://vrm.victronenergy.com/installation/{device_id}/dashboard")
        time.sleep(3)

    def check_last_updated(self):
        """
        Check when the device was last updated in local time
        """
        pass
#testing github