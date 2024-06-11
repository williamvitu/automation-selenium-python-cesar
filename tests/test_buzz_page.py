from pages.page_buzz import PageBuzz


class TestBuzzPage:

    #CT- 07 - Aba Buzz - Criar postagem
    def test_ct07_do_a_post(self, logged_setup):
        driver = logged_setup

        #ACESSANDO A PÁGINA DO BUZZ E CONFERINDO SE ESTÁ NA URL CORRETA
        buzz_page = PageBuzz(driver)
        buzz_page.go_to_buzz_page()
        assert buzz_page.is_url_buzz(), 'ESTÁ NA URL ERRADA'

        #FAZENDO UM POST E CONFERINDO SE O POST APARECER NA PÁGINA
        buzz_page.do_a_post()
        assert buzz_page.check_post(), 'Post não localizado'

    #CT-008 - Aba Buzz - Verificar contagem de likes
    def test_ct08_like(self, logged_setup):
        #LOGAR E REALIZAR UM POST
        driver = logged_setup
        buzz_page = PageBuzz(driver)
        buzz_page.go_to_buzz_page()
        assert buzz_page.is_url_buzz(), 'ESTÁ NA URL ERRADA'
        buzz_page.do_a_post()
        assert buzz_page.check_post(), 'Post não localizado'

        #DEIXAR UM LIKE NO POST CRIADO
        buzz_page.like_post()
        assert buzz_page.check_post_liked(), 'NÃO DEIXOU O LIKE'

    #CT-009 - Aba Buzz - COmpartilhar um post com comentário
    def test_ct09_share_post(self, logged_setup):
        # LOGAR E REALIZAR UM POST
        driver = logged_setup
        buzz_page = PageBuzz(driver)
        buzz_page.go_to_buzz_page()
        assert buzz_page.is_url_buzz(), 'ESTÁ NA URL ERRADA'
        buzz_page.do_a_post()
        assert buzz_page.check_post(), 'Post não localizado'

        # DEIXAR UM LIKE NO POST CRIADO
        buzz_page.open_share_popup()
        assert buzz_page.is_share_popup_open(), 'POPUP NÃO ABRIU'
        buzz_page.share_post()
        assert buzz_page.check_post('COMPARTILHANDO UM TESTE'), 'Post não localizado'