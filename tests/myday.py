import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from helpers.selenium_helper import initialize_chrome_webdriver, type_text
from user_actions.myday import MyDay


class TestMyDay(unittest.TestCase):
    """
    Test case implementations for MyDay.me web application
    """

    def setUp(self) -> None:
        """
        Initialize the Chrome driver
        """
        self.client = MyDay()

    def test_valid_schedule_session(self):
        """
        Assert successful session scheduling for a professional
        """
        self.client.login()
        self.client.skip_intro()
        self.client.navigate_to_form()
        self.client.choose_date()
        self.client.choose_time()
        self.client.enter_email()
        self.client.enter_note()
        self.client.press_save()

    def test_wrong_date(self):
        pass
        # "/html/body/div[1]/span/div/div/div"

