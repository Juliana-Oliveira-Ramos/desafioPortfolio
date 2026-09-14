from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest

class TestRealizarCompraCompleta:
    def test_adicionar_um_produto_no_carrinho(self, setup_teardown):

        driver = setup_teardown
        #login
        campo_login = driver.find_element(By.ID,"user-name").send_keys("standard_user")
        campo_senha = driver.find_element(By.ID,"password").send_keys("secret_sauce")
        campo_botao_login = driver.find_element(By.ID,"login-button").click()

        #adicionar um produto no carrinho
        driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]").click()
        
        
        #verificar se o produto foi adicionado ao carrinho
        wait = WebDriverWait(driver,20)
        botao_add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'btn_inventory')]")))
        botao_add.click()
        
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]").is_displayed()

        #clicar no botao checkout
        #driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        wait = WebDriverWait(driver, 20)
        botao_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        botao_checkout.click()
        nova_pagina = driver.find_element(By.XPATH,"//*[@data-test='title']").text
        assert nova_pagina == "Checkout: Your Information"


        #preencher o formulario apos clicar e, checkout
        first_name = driver.find_element(By.ID, "first-name").send_keys("Teste")
        last_name = driver.find_element(By.ID, "last-name").send_keys("do Teste")
        postal_code = driver.find_element(By.ID, "postal-code").send_keys("200000-000")
        wait = WebDriverWait(driver,20)
        botao_continue = wait.until(EC.element_to_be_clickable((By.ID,"continue")))
        botao_continue.click()

        pagina_checkout = driver.find_element(By.XPATH, "//*[@data-test='title']").text
        assert pagina_checkout == "Checkout: Overview"

        wait = WebDriverWait(driver,20)
        botao_finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        botao_finish.click()

        pagina_inicial = driver.find_element(By.XPATH, "//*[@class='app_logo']").text
        assert pagina_inicial == "Swag Labs"
