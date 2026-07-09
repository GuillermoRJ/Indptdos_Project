from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    URL = "http://localhost:4200/"
    
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Buscar...']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-btn")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-card")
    NO_RESULTS_MSG = (By.CSS_SELECTOR, ".no-results")

    def load(self):
        self.driver.get(self.URL)

    def search(self, product_name):
        self.type_text(product_name, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)

    def get_product_count(self):
        from selenium.webdriver.support import expected_conditions as EC
        try:
            # Espera a que los productos sean visibles
            elements = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARDS))
            return len(elements)
        except:
            return 0
        
    def get_no_results_message(self):
        return self.get_text(*self.NO_RESULTS_MSG)