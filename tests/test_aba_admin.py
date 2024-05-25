
import pytest
import logging
from time import sleep

from selenium.webdriver.support     import expected_conditions as ec

from util import constants
from pages.page_admin import AdminPage

# @pytest.fixture(scope="class", autouse=True)
# def before_after_all():
#     logging.info(f"[SETUP] Starting Suite:   {__name__}")
#     yield 
#     logging.info(f"[TEARDOWN] Starting Suite:   {__name__}")

class TestAbaAdmin:

    def test_login_page_success_for_standard_user(self, logged_setup):
        driver = logged_setup
        page_admin = AdminPage(driver)
        sleep(5)
        page_admin.clicar_menu_adm()
        sleep(5)
        
        
    


       