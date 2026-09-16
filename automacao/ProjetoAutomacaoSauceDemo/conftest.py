import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    #setup
    #global driver
    options = webdriver.ChromeOptions()
    
    # se estiver no action 
    if os.getenv("CI") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")






    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    #driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver

    driver.quit()