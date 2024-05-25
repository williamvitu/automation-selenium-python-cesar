
import pytest
import logging
import time

from pages                          import LoginPage
from selenium.webdriver.support     import expected_conditions as ec

from util import constants

@pytest.fixture(scope="class", autouse=True)
def before_after_all():
    logging.info(f"[SETUP] Starting Suite:   {__name__}")
    yield 
    logging.info(f"[TEARDOWN] Starting Suite:   {__name__}")

class TestAbaAdmin:

    def test_login_page_success_for_standard_user(self, driver):
        logging.info("Teste1")
        pass

    def test_login2_page_success_for_standard_user(self, driver):
        logging.info("Teste2")
        pass


       