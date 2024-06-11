import random
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from util import constants
from pages.page_object import PageObject
import time

class AdminPage(PageObject):
    
    lista_usuarios = (By. XPATH, '//div[@class="oxd-table-card --mobile"]')
    
    base_url = f"{constants.BASE_URL}/admin/viewSystemUsers"

    def __init__(self, driver):
        super(AdminPage, self).__init__(driver=driver)

    def acessar_menu_admin(self):
        self.driver.get(self.base_url) 

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

    def resetar_pesquisa_por_usuario(self):
        
        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
        ).click()

        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
        ).send_keys(constants.NICK_NAME_ADMIN)

        self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
        ).click()

        self.driver.find_element(
            By.XPATH, '//*[contains(@type, "button") and contains(@class, "oxd-button oxd-button--medium oxd-button--ghost")]'
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

    def verificar_qtd_de_usuarios(self):
        # number_of_users = self.driver.find_element(By.XPATH, '//span[@class="oxd-text oxd-text--span"]')
        number_of_users = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span')
        return number_of_users.text

    def extrair_numero_da_string(self):
        qtd_string = self.verificar_qtd_de_usuarios()
        numero_string = re.findall(r'\d+', qtd_string)
        qtd_usuarios = ''.join(numero_string)
        return qtd_usuarios

    def deletar_um_usuario(self):
        itens = self.driver.find_elements(By.XPATH, '//*[@class="oxd-icon bi-trash"]')
        indice_aleatorio = random.randint(0, len(itens) - 1)
        usuario = itens[indice_aleatorio]
        usuario.click()
        self.driver.find_element(By. XPATH, '//*[@class="oxd-icon bi-trash oxd-button-icon"]').click()
        
    def verificar_qtd_usaurios(self):
        qtd_atual = self.extrair_numero_da_string()
        return qtd_atual
