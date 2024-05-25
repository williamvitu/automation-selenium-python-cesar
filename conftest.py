import pytest
import logging

from selenium import webdriver
from pages.page_login    import LoginPage


@pytest.fixture
def logged_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    login_obj = LoginPage(driver)
    yield login_obj.login()
    driver.quit()