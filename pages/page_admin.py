import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from util import constants
from pages.page_object import PageObject

class AdminPage(PageObject):

    def __init__(self, driver):
        super(AdminPage, self).__init__(driver=driver)

    def clicar_menu_adm(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
        ).click()

        self.driver.find_element(
            By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        ).click()

        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
        ).click()

        self.driver.find_element(
            By.XPATH, "//*[contains(text(),'Admin')]"
        ).click()

        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input'
        ).send_keys(constants.NEW_USER)

        sugestao = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'carlos roberto junior')]"))
        )
        sugestao.click()
        
        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'
        ).click()
        
        self.driver.find_element(
            By.XPATH, '//*[contains(text(), "Enabled")]'
        ).click()
        
        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input'
        ).send_keys(constants.NEW_NICK_NAME)
        
        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'
        ).send_keys(constants.NEW_PASSWORD)
        
        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'
        ).send_keys(constants.CONFIRM_NEW_PASSWORD)
        
        self.driver.find_element(
            By.XPATH, "//button[@type='submit']"
        ).click()

    def validar_fitro_do_admin(self):
        
        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
        ).click()
        
        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
        ).send_keys(constants.NICK_NAME_ADMIN)

        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
        ).click()
        
        elemento = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'
        )
        return elemento.text

    def deletar_usuario(self):
        """Deletar usuario"""
        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
        ).click()

        lista = self.driver.find_elements(
            By.XPATH, '//i[@class="oxd-icon bi-trash"]'
        )
        lista[0].click()
    
        deletar_usuario = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'))
        )
        deletar_usuario.click()

        WebDriverWait(self.driver, 2).until(
            EC.alert_is_present((By.XPATH, '//div[@id="oxd-toaster_1"]'))
        )
       