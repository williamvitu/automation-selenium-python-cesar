from selenium.webdriver.common.by import By


from util import constants
from pages.page_object import PageObject

class PinPage(PageObject):
        
    base_url = f"{constants.BASE_URL}/pim/viewEmployeeList"
    
  
    def __init__(self, driver):
        super(PinPage, self).__init__(driver=driver)
       

    def go_to_pin_menu(self):
        self.driver.get(self.base_url)  
    
     

   
