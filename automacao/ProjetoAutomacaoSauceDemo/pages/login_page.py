import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    def __init__(self,driver) :
        super().__init__(driver)  
        #self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID,"login-button")
        self.error_message_login = (By.XPATH, "//div[@class='error-message-container error']")

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)
        WebDriverWait(self.driver, 10).until(EC.url_contains("inventory.html"))

    def verificar_mensagem_erro_login(self):
        self.verificar_se_elemento_existe(self.error_message_login)

    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        texto_esperado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi '{texto_encontrado}', mas era esperado o texto '{texto_esperado}'."
        


