import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage



@pytest.mark.usefixtures("setup_teardown")
class TestLoginValido:
    def test_login_valido(self,setup_teardown):
        driver = setup_teardown
        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_com_sucesso()