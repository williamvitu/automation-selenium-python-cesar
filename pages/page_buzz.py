from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.page_object import PageObject


class PageBuzz(PageObject):

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'               #URL DO BUZZ
    buzz_button = (By.XPATH, '//a[@href="/web/index.php/buzz/viewBuzz"]')                       #BOTÃO PARA ACESSAR URL
    input_post = (By.CLASS_NAME, 'oxd-buzz-post-input')                                         #CAMPO PARA DIGITAR O POST
    post_button = (By.XPATH, '//button[@type="submit"]')                                        #BOTÃO PARA POSTAR
    post_text_element = (By.CSS_SELECTOR, '.orangehrm-buzz-post-body-text')                     #ELEMENTOS POSTADOS
    like_heart_button_elements = (By.ID, 'heart-svg')                                           #ELEMENTO DOS LIKES POSTADOS
    number_like_button = (By.XPATH, '(//div[@class="orangehrm-buzz-stats-row"])[1]')            #ELEMENTOS COM OS NUMEROS DE LIKE
    share_post_open_elements = (By.XPATH, '//i[@class="oxd-icon bi-share-fill"]')               #ELEMENTO DOS SHARE
    share_popup_title = (By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-text--card-title"]')   #TITULO DO POPUP DE COMPARTILHAMENTO
    share_popup_button = (By.XPATH, '//button[normalize-space()="Share"]')                      #BOTÃO DE COMPARTILHAR


    def __init__(self, driver):
        super(PageBuzz, self).__init__(driver=driver)

    #FUNÇÃO PARA ACESSAR A PÁGINA DO BUZZ
    def go_to_buzz_page(self):
        self.driver.find_element(*self.buzz_button).click()

    #FUNÇÃO PARA CONFERIR SE ESTÁ NA URL DO BUZZ
    def is_url_buzz(self):
        return self.driver.current_url == self.url


    #FUNÇÃO PARA FAZER UM POST
    def do_a_post(self):
        self.driver.find_element(*self.input_post).send_keys('TESTANDO A CRIAÇÃO DO POST')
        self.driver.find_element(*self.post_button).click()

    #FUNÇÃO PARA CHECAR SE O POST FEITO ESTÁ NA PÁGINA
    def check_post(self, message='TESTANDO A CRIAÇÃO DO POST'):
        all_posts = self.driver.find_elements(*self.post_text_element)
        return all_posts[0].text == message

    #FUNÇÃO PARA DEIXAR O LIKE NO PRIMEIRO POST DA LISTA
    def like_post(self):
        all_like_posts = self.driver.find_elements(*self.like_heart_button_elements)
        all_like_posts[0].click()
        self.driver.refresh()

    #FUNÇÃO PARA CONFERIR SE O LIKE FOI ADICIONADO, RETORNA TRUE SE O VALOR FOR IGUAL A 1
    def check_post_liked(self):
        number_like = self.driver.find_element(*self.number_like_button).text[0]
        number_like_int = int(number_like)
        return number_like_int == 1

    #FUNÇÃO PARA ABRIR O POPUP PARA COMPARTILHAR UMA MENSAGEM
    def open_share_popup(self):
        all_share_button = self.driver.find_elements(*self.share_post_open_elements)
        all_share_button[0].click()

    # FUNÇÃO PARA CONFERIR SE O POPUP PARA COMPARTILHAR UMA MENSAGEM ABRIU
    def is_share_popup_open(self):
        title_share_popup = self.driver.find_element(*self.share_popup_title)
        wait = WebDriverWait(self.driver, timeout=3)
        wait.until(lambda d : title_share_popup.is_displayed())
        return title_share_popup.text == 'Share Post'

    #FUNÇÃO PARA COMPARTILHAR UM POSTO DIGIANDO UMA MENSAGEM
    def share_post(self):
        share_post_elements = self.driver.find_elements(*self.input_post)
        share_post_elements[1].send_keys('COMPARTILHANDO UM TESTE')
        self.driver.find_element(*self.share_popup_button).click()
        self.driver.refresh()








