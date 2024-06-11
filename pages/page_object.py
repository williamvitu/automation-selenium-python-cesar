
from selenium.webdriver.chrome.webdriver import WebDriver


class PageObject:

    def __init__(self, driver: WebDriver =None):
        self.driver = driver
        