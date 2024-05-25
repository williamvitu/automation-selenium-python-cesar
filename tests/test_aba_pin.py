
import time
import pytest
from pages.page_pin import PinPage

class TestAbaPin:

    @pytest.mark.pin
    def test_edit_employee_name(self, logged_setup):
        page_pin = PinPage(logged_setup)
        page_pin.go_to_pin_menu()
        page_pin.click_on_edit_employee_button()
        page_pin.edit_employee_name()
        page_pin.driver.refresh()


