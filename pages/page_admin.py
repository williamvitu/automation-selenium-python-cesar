from selenium.webdriver.common.by import By


from util import constants

from pages.page_object import PageObject

class AdminPage(PageObject):

    def __init__(self, driver):
        super(AdminPage, self).__init__(driver=driver)

    def clicar_menu_adm(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()