import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless") # Descomentar para integración continua (CI/CD)
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Obligamos a que TODAS las esperas sean explícitas
    driver.implicitly_wait(0) 
    
    yield driver
    
    # Teardown: cerrar navegador tras la prueba
    driver.quit()