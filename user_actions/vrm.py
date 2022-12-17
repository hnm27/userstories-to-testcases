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

    def get_installation_by_id(self, device_id: int):
        """
        Get an installation by inputting the id of the installation
        Args:
            device_id: str (unique)
        """
        self.driver.get(f"https://vrm.victronenergy.com/installation/{device_id}/dashboard")
        time.sleep(3)

    def check_last_updated(self):
        """
        Check if the last updated in local time is displayed
        """
        last_updated_elem = self.driver.find_element(by=By.CLASS_NAME, value='vrm-status__info__value')
        assert last_updated_elem.text is not None
        time.sleep(2)

    def check_temperatures(self):
        """
        Check if the temperature of water tank and freezer is displayed
        """
        freezer_temp_elem = self.driver.find_element(by=By.XPATH,
                                                     value='/html/body/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]')
        assert freezer_temp_elem.text is not None
        time.sleep(2)
        water_temp_elem = self.driver.find_element(by=By.XPATH,
                                                   value='/html/body/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]')
        assert water_temp_elem.text is not None
        time.sleep(2)

    def check_water_tank_level(self):
        """
        Check if fresh water tank level is displayed
        """
        water_level_elem = self.driver.find_element(by=By.XPATH,
                                                    value='//*[@id="dashboard-wrapper"]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/span')
        assert water_level_elem.text is not None
        time.sleep(2)

    def check_alarm_logs(self, device_id: int):
        """
        Check if alarm logs are displayed to the user
        """
        self.driver.get(f"https://vrm.victronenergy.com/installation/{device_id}/alarmlogs")
        time.sleep(2)
        logs_elem = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[2]/div')
        assert logs_elem is not None
