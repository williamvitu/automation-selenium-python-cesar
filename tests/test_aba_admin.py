
import pytest
import logging
import time

from selenium.webdriver.support     import expected_conditions as ec

from util import constants
from pages.page_login import LoginPage

@pytest.fixture(scope="class", autouse=True)
def before_after_all():
    logging.info(f"[SETUP] Starting Suite:   {__name__}")
    yield 
    logging.info(f"[TEARDOWN] Starting Suite:   {__name__}")

class TestAbaAdmin:

    def test_login_page_success_for_standard_user(self, logged_setup):
        driver = logged_setup
        time.sleep(10)
        
        
        
    


       