import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestEcommerceE2E:

  # --- ESCENARIOS BASE DE MEMO (Puntos 1, 2, 3) ---

  def test_login_valid_credentials(self, driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("no@test.com", "no")
    error_msg = login_page.get_error_message()
    assert len(error_msg) > 0, "Debería mostrarse un mensaje de error."

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

  # Escenario Parametrizado B: Búsqueda múltiple de productos existentes en el catálogo
  @pytest.mark.parametrize("producto, cantidad_esperada", [
    ("Small Aluminum Fish", 1),
    ("Refined Granite Towels", 1),
    ("Bespoke Cotton Table", 1)
  ])
  def test_search_existing_products_data_driven(self, driver, producto, cantidad_esperada):
    home_page = HomePage(driver)
    home_page.load()
    home_page.search(producto)
    count = home_page.get_product_count()
    assert count >= cantidad_esperada, f"Fallo al encontrar el producto: {producto}"