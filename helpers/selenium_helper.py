import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def initialize_webdriver() -> WebDriver:
    """
    Initialize the Selenium webdriver
    Returns:
        Selenium.Webdriver
    """
    return webdriver.Chrome(ChromeDriverManager().install()) # for chrome users
    # return webdriver.Firefox() # for firefox users


def initialize_headless_driver() -> WebDriver:
    """
    Initialize a headless chrome webdriver
    Returns:
         selenium.WebDriver
    """
    opts = Options()
    opts.headless = True
    driver = Chrome(options=opts, executable_path='chromedriver.exe')
    return driver


def type_text(element: WebElement, text: str):
    """
    Type the text in the field (element)
    Args:
        element : WebElement
        text : str
    """
    for character in text:
        element.send_keys(character)
        time.sleep(0.2)
