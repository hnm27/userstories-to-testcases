import time
import unittest

from selenium.webdriver.common.by import By

from user_actions.vrm import VRM


class TestVRM(unittest.TestCase):
    """
    Test case implementations for MyDay.me web application
    """
    connected_to_device = False

    def setUp(self) -> None:
        """
        Initialize the Chrome driver
        """
        self.client = VRM()

    def test_user_can_monitor_device_info(self):
        """
        Assert user can monitor device infor for a valid device id
        """
        valid_device_id = 151734
        self.client.load_app()
        self.client.navigate_to_device_list()
        self.client.get_installation_by_id(device_id=valid_device_id)
        self.client.check_last_updated()
        self.client.check_temperatures()
        self.client.check_water_tank_level()
        self.client.check_alarm_logs(device_id=valid_device_id)

    def test_no_access_to_device(self):
        """
        Assert user can monitor device infor for a valid device id
        """
        invalid_device_id = 123456
        self.client.load_app()
        self.client.navigate_to_device_list()
        self.client.get_installation_by_id(device_id=invalid_device_id)
        time.sleep(3)
        error_elem = self.client.driver.find_element(by=By.XPATH,
                                                     value='/html/body/div[2]/div/div[1]/div/div/p/span')
        assert error_elem is not None

    @unittest.skipIf(not connected_to_device, "Skipping test because not connected to relevant device")
    def test_device_error(self):
        """
        Assert device error is caught
        """
        invalid_device_id = 0  # insert device id
        self.client.load_app()
        self.client.navigate_to_device_list()
        self.client.get_installation_by_id(device_id=invalid_device_id)
        time.sleep(3)
        error_elem = self.client.driver.find_element(by=By.XPATH,
                                                     value='/html/body/div[2]/div/div[1]/div/div/p/span')
        assert error_elem is not None

    def test_unidentified_user(self):
        """
        Assert an invalid email or password raises an error
        """
        pass  # using the demo version of the webapp
