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
    To execute this test file:
        1. Create an account on https://app.myday.me if you don't have one already.
        1. Insert email and password in the fields below.
    """

    def setUp(self) -> None:
        """
        Initialize the Chrome driver
        """
        self.client = MyDay()
        self.email = ""  # TODO
        self.password = ""  # TODO

    def test_event_scheduled_successfully(self):
        """
        Assert successful session scheduling for a professional
        """
        assert self.email != "" and self.password != "", "To run this test case, enter the email and password of your " \
                                                         "Myday.me account in the file TODOs"
        self.client.login(email=self.email, password=self.password)
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
        assert self.email != "" and self.password != "", "To run this test case, enter the email and password of your " \
                                                         "Myday.me account in the file TODOs"
        self.client.login(email=self.email, password=self.password)
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
        assert self.email != "" and self.password != "", "To run this test case, enter the email and password of your " \
                                                         "Myday.me account in the file TODOs"
        self.client.login(email=self.email, password=self.password)
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
        assert self.email != "" and self.password != "", "To run this test case, enter the email and password of your " \
                                                         "Myday.me account in the file TODOs"
        self.client.login(email=self.email, password=self.password)
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
        assert self.email != "" and self.password != "", "To run this test case, enter the email and password of your " \
                                                         "Myday.me account in the file TODOs"
        success = False
        self.client.login(email=self.email, password=self.password)
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
