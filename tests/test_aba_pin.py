
import time
import pytest
import logging
from pages.page_pin import PinPage

class TestAbaPin:

    def test_edit_employee_name(self, logged_setup):
        page_pin = PinPage(logged_setup)
        page_pin.go_to_pin_menu()
        page_pin.click_on_edit_employee_button()
        page_pin.edit_employee_name()
        logging.info(page_pin.get_employee_name())
        assert "TEST" in page_pin.get_employee_name()

    @pytest.mark.pin
    def test_reset_search(self, logged_setup):
        page_pin = PinPage(logged_setup)
        page_pin.go_to_pin_menu()
        page_pin.send_keys_on_employee_name_filter("vitor")
        page_pin.send_keys_on_employee_supervisor_name_filter("teste")
        time.sleep(5)
