from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class TesteAdicionarDoisPNC:
    def teste_adicionar_dois_produtos_no_carrinho(self,setup_teardown):
        driver = setup_teardown
        wait = WebDriverWait(driver, 20)

        campo_login = driver.find_element(By.ID, "user-name").send_keys("standard_user")
        campo_senha = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        campo_botao = driver.find_element(By.ID, "login-button").click()

        #adicionar primeiro produto e validar
        
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-test='add-to-cart-sauce-labs-backpack']"))).click()

        #validar o carrinho
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@class='shopping_cart_link']"))).click()
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'Sauce Labs Backpack')]").is_displayed()

        #voltar para a vitrine 
        driver.find_element(By.ID,"continue-shopping").click()


        # adicionar segundo produto
        element = wait.until(EC.presence_of_element_located((By.NAME, "add-to-cart-sauce-labs-bike-light")))
        driver.execute_script("arguments[0].scrollIntoView();", element)  # garante que o botão está visível na tela
        wait.until(EC.element_to_be_clickable((By.NAME, "add-to-cart-sauce-labs-bike-light"))).click()

        # abrir o carrinho uma única vez
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link"))).click()

        # validar badge
        badge = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-test='shopping-cart-badge']"))).text
        assert int(badge) == 2
