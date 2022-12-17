import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
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

    def test_event_scheduled_successfully(self):
        """
        Assert successful session scheduling for a professional
        """
        self.client.login()
        # assert you are logged in as a Professional
        assert self.client.driver.current_url == "https://app.myday.me/professional/calendar"
        time.sleep(2)
        self.client.skip_intro()
        self.client.navigate_to_form()
        self.client.choose_date()
        self.client.choose_time()
        self.client.enter_email()
        self.client.enter_note()
        self.client.press_save()

        # assert the session was scheduled successfully
        notification = self.client.driver.find_element(by=By.XPATH, value="/html/body/div/span/div/div/div").text
        assert "Success" in notification

    def test_unidentified_professional(self):
        """
        An invalid email or password produces a login error
        """
        self.client.login(email="Invalid", password="Invalid")
        # assert an error was alerted to the user
        notification = self.client.driver.find_element(by=By.XPATH, value="/html/body/div/span/div/div/div").text
        assert "error" in notification

    def test_invalid_date_field(self):
        """
        An invalid date (in the past) entered should produce an error
        """
        self.client.login()
        # assert you are logged in as a Professional
        assert self.client.driver.current_url == "https://app.myday.me/professional/calendar"

        self.client.skip_intro()
        self.client.navigate_to_form()
        self.client.choose_date(past=True)
        self.client.choose_time()
        self.client.enter_email()
        self.client.enter_note()
        self.client.press_save()

        # assert the session was scheduled successfully
        notification = self.client.driver.find_element(by=By.XPATH, value="/html/body/div/span/div/div/div").text
        assert "error" in notification

    def test_invalid_time_field(self):
        """
        An invalid date (in the past) entered should produce an error
        """
        self.client.login()
        # assert you are logged in as a Professional
        assert self.client.driver.current_url == "https://app.myday.me/professional/calendar"

        self.client.skip_intro()
        self.client.navigate_to_form()
        self.client.choose_date(past=False)
        self.client.choose_time(invalid=True)
        self.client.enter_email()
        self.client.enter_note()
        self.client.press_save()

        # assert the session was scheduled successfully
        notification = self.client.driver.find_element(by=By.XPATH, value="/html/body/div/span/div/div/div").text
        assert "error" in notification

    def test_invalid_client_email(self):
        """
        An invalid date (in the past) entered should produce an error
        """
        self.client.login()
        # assert you are logged in as a Professional
        assert self.client.driver.current_url == "https://app.myday.me/professional/calendar"

        self.client.skip_intro()
        self.client.navigate_to_form()
        self.client.choose_date(past=False)
        self.client.choose_time(invalid=False)
        self.client.enter_email(email="aninvalidemail@gmail.com")
        self.client.enter_note()
        self.client.press_save()

        # assert the session was scheduled successfully
        notification = self.client.driver.find_element(by=By.XPATH, value="/html/body/div/span/div/div/div").text
        assert "error" in notification

    def test_no_clients_chosen(self):
        """
        No clients chosen should not allow professionals to create an event
        """
        success = False
        self.client.login()
        # assert you are logged in as a Professional
        assert self.client.driver.current_url == "https://app.myday.me/professional/calendar"

        self.client.skip_intro()
        self.client.navigate_to_form()
        self.client.choose_date(past=False)
        self.client.choose_time(invalid=False)
        self.client.enter_email(email="")
        self.client.enter_note()
        try:
            self.client.press_save()
        except ElementClickInterceptedException:
            success = True  # element cannot be clicked
        finally:
            assert success
