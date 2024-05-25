from selenium.webdriver.common.by import By
from selenium import webdriver

from util import constants

class LoginPage:
        
    base_url = constants.BASE_URL

    def __init__(self) -> None:
        self.input_username     = (By.NAME, 'username')
        self.input_password     = (By.NAME, 'password')
        self.button_login       = (By.XPATH,'//button[@type="submit"]')
  
       

    def login(self):

        driver = webdriver.Chrome()
        driver.implicitly_wait(15)
        driver.get(self.base_url)  
        driver.find_element(*self.input_username).send_keys(constants.USER_STANDARD)
        driver.find_element(*self.input_password).send_keys(constants.USER_PASSWORD)
        driver.find_element(*self.button_login).click()
        return driver