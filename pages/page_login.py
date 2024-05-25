from selenium.webdriver.common.by import By


from util import constants

from pages.page_object import PageObject

class LoginPage(PageObject):
        
    base_url = constants.BASE_URL
    input_username     = (By.NAME, 'username')
    input_password     = (By.NAME, 'password')
    button_login       = (By.XPATH,'//button[@type="submit"]')
  
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver=driver)
        # self.driver = driver
       

    def login(self):
        self.driver.get(self.base_url)  
        self.driver.find_element(*self.input_username).send_keys(constants.USER_STANDARD)
        self.driver.find_element(*self.input_password).send_keys(constants.USER_PASSWORD)
        self.driver.find_element(*self.button_login).click()
        return self.driver
     

   
