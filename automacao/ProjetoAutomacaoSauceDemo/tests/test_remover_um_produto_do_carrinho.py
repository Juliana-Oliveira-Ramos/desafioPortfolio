from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time



@pytest.mark.usefixtures("setup_teardown")
class TestRemoverProdutoDoCarrinho:
    def test_remover_um_produto_do_carrinho(self,setup_teardown):
        driver = setup_teardown
        wait = WebDriverWait(driver, 20)
        #login
        campo_login = driver.find_element(By.ID,"user-name").send_keys("standard_user")
        campo_senha = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        botao_login = driver.find_element(By.ID, "login-button").click()
        
        driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()

        # Verificar se o produto foi adicionado ao carrinho
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'Sauce Labs Backpack')]").is_displayed()
        
        # Voltar para a página de produtos
        driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()

        # Tentar encontrar e clicar no botão "Remove"
        try:
            botao_remove = wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack")))
            botao_remove.click()
            time.sleep(1)  

            # Verificar se o produto foi removido do carrinho
            driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
            with pytest.raises(Exception):
                driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'Sauce Labs Backpack')']")
        except Exception as e:
            pytest.fail(f"Não foi possível remover o produto do carrinho: {e}")


        






        
        