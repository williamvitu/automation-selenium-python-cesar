from time import sleep
import pytest
import logging
from selenium.webdriver.support import expected_conditions as ec
from util import constants
from pages.page_admin import AdminPage


@pytest.fixture(scope="class", autouse=True)
def before_after_all():
    logging.info(f"[SETUP] Starting Suite:   {__name__}")
    yield 
    logging.info(f"[TEARDOWN] Starting Suite:   {__name__}")

class TestAbaAdmin:

    def test_resetar_pesquisa_por_usuario(self, logged_setup):
        driver = logged_setup
        page_admin = AdminPage(driver)
        page_admin.acessar_menu_admin()
        page_admin.verificar_qtd_de_usuarios()
        qtd_antes = page_admin.extrair_numero_da_string()
        page_admin.resetar_pesquisa_por_usuario()
        page_admin.resetar_pesquisa_por_usuario()
        page_admin.verificar_qtd_de_usuarios()
        qtd_depois = page_admin.extrair_numero_da_string()
        assert qtd_antes == qtd_depois

    def test_validar_filtro(self, logged_setup):
        driver = logged_setup
        page_admin = AdminPage(driver)
        assert page_admin.validar_fitro_do_admin() == constants.NICK_NAME_ADMIN

    def test_deletar_usuario(self, logged_setup):
        driver = logged_setup
        page_admin = AdminPage(driver)
        page_admin.acessar_menu_admin()
        page_admin.verificar_qtd_de_usuarios()
        qtd = page_admin.extrair_numero_da_string()
        page_admin.deletar_um_usuario()
        qtd_atual = page_admin.verificar_qtd_usaurios()
        assert qtd_atual < qtd