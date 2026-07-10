import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestEcommerceE2E:

  def test_login_success(self, driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(
      "admin@ecommerce.com",
      "adminpassword"
    )
    home_page = HomePage(driver)
    assert driver.current_url == home_page.URL or "dashboard" in driver.current_url or "login" not in driver.current_url

  def test_login_invalid_credentials(self, driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("no@test.com", "no")
    error_msg = login_page.get_error_message()
    assert len(error_msg) > 0, "Debería mostrarse un mensaje de error."

  @pytest.mark.parametrize("username, password, expected_error", [
    ("", "admin123", "El usuario es requerido"),
    ("jorge@test.com", "", "La contraseña es requerida"),
    ("usuario_invalido", "pass", "incorrectas")
  ])
  def test_login_validation_data_driven(self, driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    error_msg = login_page.get_error_message()
    assert len(error_msg) > 0, "Debería lanzar un mensaje de validación en el formulario."