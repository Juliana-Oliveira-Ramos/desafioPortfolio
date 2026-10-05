from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import pytest
import logging


@pytest.mark.usefixtures("setup_teardown")
class TestAdicionarProdutoCarrinho:
    def test_adicionar_um_produto_carrinho(self, setup_teardown):
        driver = setup_teardown
        wait = WebDriverWait(driver, 10)

        # login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # abrir página do produto
        driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]").click()

        # adicionar produto ao carrinho
        try:
            botao_add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'btn_inventory')]")))
            botao_add.click()
        except StaleElementReferenceException:
            botao_add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'btn_inventory')]")))
            botao_add.click()

        # abrir carrinho
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

        # validar produto no carrinho (com try/except para evitar stale)
        try:
            produto = driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]")
            assert produto.is_displayed()
        except StaleElementReferenceException:
            produto = driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]")
            assert produto.is_displayed()
