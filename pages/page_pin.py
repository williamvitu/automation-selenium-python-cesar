
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from util import constants
from pages.page_object import PageObject

import random
import logging
import time

class PinPage(PageObject):
        
    base_url = f"{constants.BASE_URL}/pim/viewEmployeeList"
    
    # PIM - MAIN PAGE
    panel_employee_details = (By.XPATH, '//div[contains(@class, "orangehrm-edit-employee-content")]')
    panel_employee_loader = (By.CLASS_NAME, 'oxd-form-loader') 
    
    table_employee_card_list  = (By.CSS_SELECTOR, '[role="row"]')
    
    input_employee_name_filter  = (By.XPATH, '//*[@class="oxd-autocomplete-text-input oxd-autocomplete-text-input--active"]//input')  
    input_employee_id = (By.CSS_SELECTOR,'input.oxd-input.oxd-input--active:not([placeholder]):empty')
    input_employee_supervisor_name_filter = (By.CSS_SELECTOR, '.oxd-autocomplete-text-input.oxd-autocomplete-text-input--active input[placeholder]')
    input_employee_list = (By.CSS_SELECTOR, '[class="oxd-input-group oxd-input-field-bottom-space"]')
    
    
    button_reset = (By.XPATH, '//button[normalize-space()="Reset"]')
    
    dropdown_list = (By.CSS_SELECTOR, '[class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]')
    dropdown_options = (By.CSS_SELECTOR, '[role="option"] span')

    dropdown_filters = (By.CSS_SELECTOR, '[class="oxd-select-text oxd-select-text--active"]')
    list_employement_status = (By.CSS_SELECTOR, '[role="listbox"]')
    # PIM - EMPLOYEE PROFILE DETAILS
    label_employee_name = (By.CSS_SELECTOR,'h6[class="oxd-text oxd-text--h6 --strong"]')
    input_employee_name = (By.NAME, 'firstName')
    buttons_save_list = (By.CSS_SELECTOR, '[class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
    
    def __init__(self, driver):
        super(PinPage, self).__init__(driver=driver)


    def go_to_pin_menu(self):
        self.driver.get(self.base_url)  
    
    def send_keys_on_employee_name_filter(self, text: str):
        self.driver.find_element(*self.input_employee_name_filter).send_keys(text)
    
    def send_keys_on_employee_id(self, text: str):
        self.driver.find_element(*self.input_employee_id).send_keys(text)

    def send_keys_on_employee_supervisor_name(self, text: str):
        self.driver.find_elements(*self.input_employee_name_filter)[1].send_keys(text)

    def click_and_select_option_on_employement_status(self):
        self.driver.find_elements(*self.input_employee_list)[2].click()
        self.select_any_option_dropdown()

    def click_on_reset_button(self):
        self.driver.find_element(*self.button_reset).click()

    def click_and_select_option_on_include(self):
        self.driver.find_elements(*self.input_employee_list)[3].click()
        self.select_any_option_dropdown()

    def click_and_select_option_on_title(self):
        self.driver.find_elements(*self.input_employee_list)[5].click()
        self.select_any_option_dropdown()

    def click_and_select_option_on_sub_unit(self):
        self.driver.find_elements(*self.input_employee_list)[6].click()
        self.select_any_option_dropdown()

    def click_on_edit_employee_button(self):
        cards_list = self.driver.find_elements(*self.table_employee_card_list)
        card = random.choice(cards_list)
        card.click()

    def select_any_option_dropdown(self):
        employements =  self.driver.find_elements(*self.dropdown_options)
        employement = random.choice(employements)
        employement.click()

    def get_employee_name(self):
        # Tentei vários wait's do expected_conditions, por algum motivo não funcionam, deixei o time.sleep mesmo
        # employee_name = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.label_employee_name))
        time.sleep(6)
        return self.driver.find_element(*self.label_employee_name).text


    def edit_employee_name(self):
        
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.panel_employee_loader))

        e = self.driver.find_element(*self.input_employee_name)

        e.send_keys("TEST")
        
        buttons = self.driver.find_elements(*self.buttons_save_list)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(buttons[0]))

        buttons[0].click()
    
    def validate_all_filters_reset(self) -> bool:
        employee_fields = self.driver.find_elements(*self.input_employee_list)
        for index, employee_field in enumerate(employee_fields):
            
            if index in [2,3,5,6]:
                child_element = employee_field.find_element(By.CLASS_NAME, "oxd-select-text-input")
                if index == 3:
                    assert 'Current Employees Only' in child_element.text
                    continue

                assert 'Select' in child_element.text            
        
        return True

        
