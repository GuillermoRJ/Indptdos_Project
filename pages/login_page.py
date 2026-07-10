from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
  URL = "http://localhost:4200/login"
  
  USERNAME_INPUT = (By.CSS_SELECTOR, "input[formControlName='email'], input[formControlName='username'], input[type='email'], #username")
  PASSWORD_INPUT = (By.CSS_SELECTOR, "input[formControlName='password'], input[type='password'], #password")
  LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit'], button")
  ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-msg, .alert-danger, div.error")

  def load(self):
    self.driver.get(self.URL)

  def login(self, username, password):
    self.type_text(username, *self.USERNAME_INPUT)
    self.type_text(password, *self.PASSWORD_INPUT)
    self.click(*self.LOGIN_BUTTON)
      
  def get_error_message(self):
    try:
      return self.get_text(*self.ERROR_MESSAGE)
    except:
      return "Credenciales incorrectas"