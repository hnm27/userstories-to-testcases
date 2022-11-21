import unittest

from user_actions.vrm import VRM


class TestVRM(unittest.TestCase):
    """
    Test case implementations for MyDay.me web application
    """

    def setUp(self) -> None:
        """
        Initialize the Chrome driver
        """
        self.client = VRM()

    def test_event_scheduled_successfully(self):
        """
        Assert successful session scheduling for a professional
        """
        self.client.load_app()
        self.client.navigate_to_device_list()
        self.client.get_installation_by_id(device_id=151734)
        self.client.check_last_updated()
