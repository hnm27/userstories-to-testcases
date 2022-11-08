import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from helpers.selenium_helper import initialize_chrome_webdriver, type_text


class MyDay(unittest.TestCase):
    """
    Test case implementations for MyDay.me web application
    """

    def setUp(self) -> None:
        """
        Initialize the Chrome driver
        """
        self.driver = initialize_chrome_webdriver()

    def test_valid_schedule_session(self):
        """
        Assert successful session scheduling for a professional
        """
        # login to schedule a session with correct credentials
        self.login()
        # wait for the page to load
        time.sleep(3)

        try:
            # skip introduction (press skip)
            self.driver.find_element(by=By.XPATH,
                                     value="/html/body/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/a").click()
            time.sleep(2)
        except NoSuchElementException as e:
            print(f"No Skip intro button: {e}")

        self.navigate_to_form()
        self.choose_date()
        self.choose_time()
        self.enter_email()

        # add note
        note_field = self.driver.find_element(by=By.XPATH,
                                              value="/html/body/div[1]/div[2]/div[3]/div/form/div[2]/div[11]/div[2]/div/textarea")
        note_field.send_keys("This is a test!")
        # press save
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div[1]/div[2]/div[3]/div/form/div[2]/div[12]/button").click()
        time.sleep(3)

    def test_wrong_date(self):
        pass
        # "/html/body/div[1]/span/div/div/div"

    def login(self, email: str = "humaidalimollah73@gmail.com", password: str = "userstoriestotestcases"):
        """
        Assert correct login behavior
        """
        # Navigate to login page
        self.driver.get("https://app.myday.me/auth/signin")
        # wait for the page to load
        time.sleep(2)
        # assert you are on the correct page
        assert "MyDay" in self.driver.title
        # accept terms (Click on "I understand")
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div/div[3]/div/div/div/div/button[1]").click()
        # switch to professional
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/main/div/div/div[1]/div/div/div/div[2]/div/a[2]").click()
        # type email and password
        email_field = self.driver.find_element(by=By.NAME, value="email")
        password_field = self.driver.find_element(by=By.NAME, value="password")
        type_text(element=email_field, text=email)
        type_text(element=password_field, text=password)
        # submit form (Click Login)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/main/div/div/div[1]/div/div/div/form/button").click()
        # wait for the page to load
        time.sleep(2)
        # assert you are logged in as a Professional
        assert self.driver.current_url == "https://app.myday.me/professional/calendar"

    def navigate_to_form(self):
        """
        Navigate to session creation form
        """
        # click on create an event
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/div[2]/button").click()
        time.sleep(1)
        # choose option
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/div[2]/div/button[2]").click()
        time.sleep(1)

    def choose_date(self, past: bool = False):
        """
         Choose a date
         Args:
             past : bool : test for a past date by going into the previous month
        """
        # choose date
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[2]/div[3]/div/form/div[2]/div[1]/div/div/div").click()
        time.sleep(1)
        element_xpath = "/html/body/div/div[2]/div[3]/div/form/div[2]/div[1]/div/div/div/div[2]/div[1]/button[2]"
        if past:
            element_xpath = "/html/body/div[1]/div[2]/div[3]/div/form/div[2]/div[1]/div/div/div/div[2]/div[1]/button[1]"

        self.driver.find_element(by=By.XPATH,
                                 value=element_xpath).click()
        time.sleep(1)
        # choose any day
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[2]/div[3]/div/form/div[2]/div[1]/div/div/div/div[2]/div[3]/div[11]/div").click()
        time.sleep(2)

    def choose_time(self, invalid: bool = False):
        """
        Choose time period
        Args:
            invalid : bool : to insert invalid date
        """
        # choose time

        start_time = "7"  # 6am
        end_time = "11"  # 10am
        if invalid:
            start_time, end_time = end_time, start_time

        # start time 6am
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/div[2]/div/div").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,
                                 value=f"/html/body/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[{start_time}]").click()
        time.sleep(1)
        # end time 10am
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/div[4]/div/div").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,
                                 value=f"/html/body/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/div[4]/div/div/div[2]/div/div[1]/div[{end_time}]").click()
        time.sleep(1)

    def enter_email(self, email: str = "hnmmollah27@gmail.com"):
        """
        Enter email
        Args:
            email : str : to test valid email
        """
        # enter email
        email_field = self.driver.find_element(by=By.XPATH,
                                               value="/html/body/div[1]/div[2]/div[3]/div/form/div[2]/div[9]/div/div/input")
        email_field.send_keys(email)
