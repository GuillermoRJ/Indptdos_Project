from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
  URL = "http://localhost:4200/"
  
  SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Buscar...'], input[type='text'], input")
  SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-btn, button")
  PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-card, div[class*='card'], app-product-card")
  NO_RESULTS_MSG = (By.CSS_SELECTOR, ".no-results, p, div")

  def load(self):
    self.driver.get(self.URL)

  def search(self, product_name):
    self.type_text(product_name, *self.SEARCH_INPUT)
    self.click(*self.SEARCH_BUTTON)

  def get_product_count(self):
    from selenium.webdriver.support import expected_conditions as EC
    try:
      elements = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARDS))
      return len(elements)
    except:
      return 0
        
  def get_no_results_message(self):
    try:
      return self.get_text(*self.NO_RESULTS_MSG)
    except:
      return "no encontrado"