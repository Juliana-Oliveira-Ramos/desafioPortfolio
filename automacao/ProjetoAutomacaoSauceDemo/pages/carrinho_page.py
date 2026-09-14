import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CarrinhoPage(BasePage):
    def __init__(self) -> None:
        self.driver = conftest.driver
        self.item_iventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}'] ")
        self.botao_continuar_comprando(By.XPATH, "//*[@id='continue-shopping']")

    def verificar_produto_carrinho_existe(self, nome_item):
        item = (self.item_iventario[0], self.item_iventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)

    def clicar_botao_checkout(self):
        self.clicar(self.clicar_botao_checkout)

    
        