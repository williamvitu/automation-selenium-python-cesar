from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from util import constants
from pages.page_object import PageObject
from faker import Faker

import random
import logging
import time
class PinPage(PageObject):
        
    base_url = f"{constants.BASE_URL}/pim/viewEmployeeList"
    
    # PIM - MAIN PAGE
    table_employee_card_list  = (By.CSS_SELECTOR, '[role="row"]')
    input_employee_name_filter = (By.XPATH, '//input[@placeholder="Type for hints..."]')  
    input_employee_supervisor_name_filter = (By.CSS_SELECTOR, '[class="oxd-autocomplete-text-input oxd-autocomplete-text-input--active"]')
    
    # PIM - EMPLOYEE PROFILE DETAILS
    label_employee_name = (By.CSS_SELECTOR,'h6[class="oxd-text oxd-text--h6 --strong"]')
    input_employee_name = (By.NAME, 'firstName')
    buttons_save_list = (By.CSS_SELECTOR, '[class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
    
    def __init__(self, driver):
        super(PinPage, self).__init__(driver=driver)


    def go_to_pin_menu(self):
        self.driver.get(self.base_url)  
    
    def click_on_edit_employee_button(self):
        cards_list = self.driver.find_elements(*self.table_employee_card_list)
        card = random.choice(cards_list)
        card.click()

    def get_employee_name(self):
        # Esse wait também não funciona, incluí um time.sleep
        # employee_name = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.label_employee_name))
        # time.sleep(10)
        return self.driver.find_element(*self.label_employee_name).text

    def edit_employee_name(self):
        
        # Esse Wait não funciona
        e = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_employee_name))
        # Deixei esse time.sleep também
        time.sleep(5)
        e.send_keys("TEST")
        
        # Esse Wait também não funciona
        buttons = WebDriverWait(self.driver, 15).until(EC.visibility_of_all_elements_located(self.buttons_save_list))
        
        # Tentei de vários jeitos talvez seja bug no componente, não sei, deixei o teste aqui mais para conhecimento
        # Sem os 'time.sleep' nada funciona nessa página
        time.sleep(5)

        buttons[0].click()
        time.sleep(10)
        # Este wait abaixo também não funciona, impressionante, deixei o time.sleep acima
        # employee_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.label_employee_name))

        
