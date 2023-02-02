import unittest

from selenium.common import NoSuchElementException, InvalidArgumentException

from user_actions.utwente_people_page import Lepaya


class TestUtwentePeopleSearch(unittest.TestCase):
    """
    Test case implementations for Utwente people page
    """

    def setUp(self) -> None:
        """
        Initialize the Chrome driver
        """
        self.client = Lepaya()

    def test_user_can_search_for_contact_details(self):
        """
        Test user can search for info successfully
        """
        self.client.access_webpage()
        self.client.search(query='petra van den bos')
        self.client.add_filter(filter_num=3)
        self.client.get_contact_details()  # depends on search query

    def test_unidentified_employee(self):
        """
        Test invalid query search
        """
        success = False
        self.client.access_webpage()
        self.client.search(query='humaid mollah')
        try:
            self.client.get_contact_details()
        except NoSuchElementException:
            success = True
        assert success

    def test_non_matching_filter(self):
        """
        Test invalid query filter combination search
        """
        success = False
        self.client.access_webpage()
        self.client.search(query='petra van den bos')
        self.client.add_filter(filter_num=1)
        try:
            self.client.get_contact_details()
        except NoSuchElementException:
            success = True
        assert success

    def tearDown(self) -> None:
        """
        Close the driver
        """
        self.client.driver.close()