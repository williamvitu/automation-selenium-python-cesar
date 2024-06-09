import pytest
import logging
from selenium.webdriver.support import expected_conditions as ec
from util import constants
from pages.page_admin import AdminPage


# @pytest.fixture(scope="class", autouse=True)
# def before_after_all():
#     logging.info(f"[SETUP] Starting Suite:   {__name__}")
#     yield 
#     logging.info(f"[TEARDOWN] Starting Suite:   {__name__}")

class TestAbaAdmin:

    # def test_login_page_success_for_standard_user(self, logged_setup):
    #     driver = logged_setup
    #     page_admin = AdminPage(driver)
    #     page_admin.clicar_menu_adm()
    #     assert driver.current_url == constants.URL_viewSystemUsers

    # def test_validar_filtro(self, logged_setup):
    #     driver = logged_setup
    #     page_admin = AdminPage(driver)
    #     assert page_admin.validar_fitro_do_admin() == constants.NICK_NAME_ADMIN

    def test_deletar_usuario(self, logged_setup):
        driver = logged_setup
        page_admin = AdminPage(driver)
        page_admin.acessar_menu_admin()
        qtd = page_admin.verificar_qtd_de_usuarios()
        qtd_usuarios = page_admin.extrair_numero_da_string()
        print(qtd_usuarios)
        # assert qtd == '(7) Records Found'
        # page_admin.validar_usuario_excluido()