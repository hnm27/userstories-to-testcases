import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from helpers.selenium_helper import initialize_webdriver, type_text


class Lepaya:
    """
    User actions for Lepaya web application
    """

    def __init__(self) -> None:
        """
        Initialize the Chrome driver
        """
        self.filter_id = None
        self.query = None
        self.driver = initialize_webdriver()

    def access_webpage(self):
        """
        Access the webapp
        """
        self.driver.get("https://people.utwente.nl/")
        # wait for the page to load
        time.sleep(4)
        try:
            # accept cookies
            self.driver.find_element(by=By.ID, value='utwenteCookiesConsent').click()
            time.sleep(2)
            # save choice
            self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/button").click()
        except NoSuchElementException:
            print("no cookies option required")

    def search(self, query: str):
        """
        Make a query in the search bar
        """
        self.query = query
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
            self.filter_id = "filter-hoogleraren"
        elif filter_num == 2:
            self.filter_id = "filter-ondersteunend"
        else:
            self.filter_id = "filter-wetenschappers"
        self.driver.find_element(by=By.ID, value=self.filter_id).click()
        time.sleep(3)

    def get_contact_details(self):
        """
        Assert if contact details of an employee are visible
        """
        url = 'https://people.utwente.nl/'
        # we test against 1 input only - petra van den bos
        # no such url exists for input - humaid mollah
        if self.query == 'petra van den bos' and self.filter_id == "filter-wetenschappers":
            url = url + 'p.vandenbos'
        else:
            print(f"no url exists for {self.query}")
        # navigate to contact details webpage
        self.driver.get(url=url)
        time.sleep(2)
        # click contact button
        self.driver.get(url=f'{url}?tab=contact#contact')  # button is an href
        # assert display contact details
        time.sleep(2)
        info = self.driver.find_element(by=By.CLASS_NAME, value='info-block')
        assert info is not None
