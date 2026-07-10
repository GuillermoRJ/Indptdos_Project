from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    URL = "http://localhost:4200/"
    
    PRODUCT_CARDS = (By.CSS_SELECTOR, "app-products-card")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "app-products-card h3") 
    CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Cart']")
    
    def load(self):
        self.driver.get(self.URL)

    def get_product_titles(self):
        elements = self.find_elements(*self.PRODUCT_TITLES)
        return [el.text for el in elements]