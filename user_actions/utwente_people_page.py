import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from helpers.selenium_helper import initialize_chrome_webdriver, type_text


class Lepaya:
    """
    User actions for Lepaya web application
    """

    def __init__(self) -> None:
        """
        Initialize the Chrome driver
        """
        self.driver = initialize_chrome_webdriver()

    def access_webpage(self):
        """
        Access the webapp
        """
        self.driver.get("https://people.utwente.nl/")
        # wait for the page to load
        time.sleep(2)
        try:
            self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/button").click()
        except Exception:
            print("no accept button")

    def search(self, query: str):
        """
        Make a query in the search bar
        """
        search_form = self.driver.find_element(by=By.CLASS_NAME, value='input')
        search_form.send_keys(query)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div[1]/div/div[2]/div[1]/div/div/div['
                                                    '2]/form/div/button').click()
        time.sleep(3)

    def add_filter(self, filter_num: int):
        """
        Args:
            filter_num: int
        Select a filter:
        1. Full Professor
        2. Supporting staff only
        3. Faculty staff only
        """
        if filter_num == 1:
            filter_id = "filter-hoogleraren"
        elif filter_num == 2:
            filter_id = "filter-ondersteunend"
        else:
            filter_id = "filter-wetenschappers"
        self.driver.find_element(by=By.ID, value=filter_id).click()
        time.sleep(3)

    def get_contact_details(self):
        """
        Assert if contact details of a person are visible
        """
        # navigate to contact details webpage
        self.driver.find_element(by=By.CLASS_NAME, value='result__item').click()
        time.sleep(5)
        # accept cookies code giving some problems
        try:
            self.driver.find_element(by=By.CLASS_NAME, value='VfPpkd-RLmnJb').click()
            time.sleep(2)
        except NoSuchElementException:
            print("no accept button")
        # assert display contact details
        info = self.driver.find_element(by=By.CLASS_NAME, value='info-block')
        assert info is not None
