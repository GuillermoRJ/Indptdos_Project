from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "http://localhost:4200/login"
    
    # Selectores ajustados a los directivas de Angular
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[formControlName='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[formControlName='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "app-error-message")

    def load(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.find_element(*self.EMAIL_INPUT).clear()
        self.find_element(*self.EMAIL_INPUT).send_keys(email)
        
        self.find_element(*self.PASSWORD_INPUT).clear()
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        
        self.click_element(*self.SUBMIT_BUTTON)
        
    def get_error_text(self):
        return self.find_element(*self.ERROR_MESSAGE).text