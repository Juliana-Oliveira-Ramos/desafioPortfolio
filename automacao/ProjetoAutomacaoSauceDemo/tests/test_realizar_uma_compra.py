from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest





@pytest.mark.usefixtures("setup_teardown")
class TestAdicionarProdutoCarrinho:
    def test_adicionar_um_produto_carrinho(self,setup_teardown):
        driver = setup_teardown
        
        #login
        campo_login = driver.find_element(By.ID,"user-name").send_keys("standard_user")
        campo_senha = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        botao_login = driver.find_element(By.ID, "login-button").click()

       


        #adicionar um produto no carrinho
        driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]").click()


        #verificar se o produto foi adicionado ao carrinho
        wait = WebDriverWait(driver, 10)
        botao_add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'btn_inventory')]")))
        botao_add.click()

        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]").is_displayed()

        #clicar no botao checkout para finalizar as 
        wait = WebDriverWait(driver, 10)
        botao_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        botao_checkout.click()

        assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Checkout: Your Information']").is_displayed()



        