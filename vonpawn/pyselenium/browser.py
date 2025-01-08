from selenium import webdriver
from enum import Enum


class Driver(Enum):
    CHROME = 1
    FIREFOX = 2
    EDGE = 3
    CHROME_HEADLESS: 4


class Browser:

    def __init__(self, config):
        self._driver = webdriver.Chrome
        self.config = config

    def configure(self):
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def get_driver(self):
        # expose driver for page objects to run selenium operations that have not been exposed
        return self._driver

    def navigate(self, url):
        self._driver.get(url)

    def page_title_contains(self, text):
        return text in self._driver.title

    def find_element(self, by, locator):
        # move to base page?
        pass
