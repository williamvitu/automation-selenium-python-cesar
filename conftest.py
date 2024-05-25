import pytest
import logging

from selenium import webdriver
from pages    import LoginPage


@pytest.fixture
def driver():
    
    login_obj = LoginPage()
    driver = login_obj.login()
    yield driver
    driver.quit()