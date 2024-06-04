import time
import pytest
import logging
from pages.page_pin import PinPage


@pytest.fixture(scope="function")
def page_pin(logged_setup):
    page_pin = PinPage(logged_setup)
    page_pin.go_to_pin_menu()

    return PinPage(logged_setup)

class TestAbaPin:
    
    @pytest.mark.pin
    def test_edit_employee_name(self, page_pin : PinPage):
        page_pin.click_on_edit_employee_button()
        page_pin.edit_employee_name()
        page_pin.driver.refresh()
        assert "TEST" in page_pin.get_employee_name()

    @pytest.mark.pin
    def test_reset_search(self,  page_pin : PinPage):
        page_pin.send_keys_on_employee_name_filter("vitor")
        page_pin.send_keys_on_employee_id("vitor")
        page_pin.send_keys_on_employee_supervisor_name('vitor')
        page_pin.click_and_select_option_on_employement_status()
        page_pin.click_and_select_option_on_include()
        page_pin.click_and_select_option_on_sub_unit()
        page_pin.click_and_select_option_on_title()
        page_pin.click_on_reset_button()
        assert page_pin.validate_all_filters_reset()
    
    @pytest.mark.pin
    def test_employee_ordering(self,  page_pin : PinPage):
        page_pin.click_on_name_ordering_button()
        page_pin.click_on_ascending_option_for_first_name()
        assert page_pin.validate_ascending_employee_name()