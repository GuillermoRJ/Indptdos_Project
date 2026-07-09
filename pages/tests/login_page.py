from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "http://localhost:4200/login" # Ajusta a la ruta real de tu frontend Angular
    
    # Localizadores (Ajústalos a los selectores reales de tu app)
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-msg")

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type_text(username, *self.USERNAME_INPUT)
        self.type_text(password, *self.PASSWORD_INPUT)
        self.click(*self.LOGIN_BUTTON)
        
    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)