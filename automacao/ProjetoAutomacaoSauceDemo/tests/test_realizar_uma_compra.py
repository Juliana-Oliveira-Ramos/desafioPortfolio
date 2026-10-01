from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.commom.exceptions import StaleElementReferenceException
import pytest





@pytest.mark.usefixtures("setup_teardown")
class TestAdicionarProdutoCarrinho:
    def test_adicionar_um_produto_carrinho(self,setup_teardown):
        driver = setup_teardown
        
        #login
        campo_login = driver.find_element(By.ID,"user-name").send_keys("standard_user")
        campo_senha = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        botao_login = driver.find_element(By.ID, "login-button").click()

        try:
            botao_add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'btn_inventory')]")))
            botao_add.click()
        except StaleElementReferenceException:
            botao_add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'btn_inventory')]")))
            botao_add.click()

        # abrir carrinho
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        assert driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]").is_displayed()

        # checkout (com try/except)
        try:
            botao_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
            botao_checkout.click()
        except StaleElementReferenceException:
            botao_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
            botao_checkout.click()

        # validar página de checkout
        try:
            titulo = driver.find_element(By.XPATH, "//span[@class='title']").text
        except StaleElementReferenceException:
            titulo = driver.find_element(By.XPATH, "//span[@class='title']").text
        assert titulo == "Checkout: Your Information"

        # preencher formulário
        driver.find_element(By.ID, "first-name").send_keys("Teste")
        driver.find_element(By.ID, "last-name").send_keys("do Teste")
        driver.find_element(By.ID, "postal-code").send_keys("200000-000")

        # continuar (com try/except)
        try:
            botao_continue = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
            botao_continue.click()
        except StaleElementReferenceException:
            botao_continue = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
            botao_continue.click()

        # validar página de overview
        try:
            titulo_checkout = driver.find_element(By.XPATH, "//span[@class='title']").text
        except StaleElementReferenceException:
            titulo_checkout = driver.find_element(By.XPATH, "//span[@class='title']").text
        assert titulo_checkout == "Checkout: Overview"

        # finalizar compra (com try/except)
        try:
            botao_finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
            botao_finish.click()
        except StaleElementReferenceException:
            botao_finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
            botao_finish.click()

        # validar retorno à página inicial (com try/except)
        try:
            pagina_inicial = driver.find_element(By.CLASS_NAME, "app_logo").text
        except StaleElementReferenceException:
            pagina_inicial = driver.find_element(By.CLASS_NAME, "app_logo").text
        assert pagina_inicial == "Swag Labs"
