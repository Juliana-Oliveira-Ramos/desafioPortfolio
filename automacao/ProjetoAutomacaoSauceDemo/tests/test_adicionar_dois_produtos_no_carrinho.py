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

        driver.find_element(By.XPATH,"//button[@data-test='add-to-cart-sauce-labs-backpack']").click()

        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'Sauce Labs Backpack')]").is_displayed()

        driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()

        driver.find_element(By.XPATH, "//button[@name='add-to-cart-sauce-labs-bike-light']").click()
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()


        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        badge = driver.find_element(By.XPATH, "//*[@data-test='shopping-cart-badge']").text
        assert int(badge) == 2
        print(" Carrinho validado com sucesso !!!")
