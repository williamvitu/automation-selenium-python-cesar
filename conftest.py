import pytest
from selenium import webdriver
from pages.page_login    import LoginPage


@pytest.fixture
def logged_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    login_obj = LoginPage(driver)
    yield login_obj.login()
    driver.quit()