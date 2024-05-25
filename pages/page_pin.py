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

    # PIM - EMPLOYEE PROFILE DETAILS
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

       


    def edit_employee_name(self):
        fake = Faker()
        random_name = fake.name()
        # random_name = "Aaron"
        logging.info(random_name)
            
        # Por algum motivo, esse Wait não funciona direito, está intermitente
        e = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_employee_name))
        # Por algum motivo, locator.clear() não funcionava, tive que colocar este CTRL+A e posteriormente apagar
        # Vou deixar o time.sleep comentado, mas só assim o teste funciona.
        # time.sleep(5)
        # e.send_keys(Keys.CONTROL+"A")
        # time.sleep(5)
        e.send_keys(Keys.BACKSPACE*len(e.text))
        # time.sleep(10)
        # e.clear()
        e.send_keys(random_name)
        time.sleep(10)
        buttons = self.driver.find_elements(*self.buttons_save_list)
       
        save_button = buttons[0]
        save_button.click()
        
