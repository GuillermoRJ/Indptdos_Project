import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestEcommerceE2E:

  # --- ESCENARIOS BASE DE MEMO (Puntos 1, 2, 3) ---

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

  def test_search_empty_string(self, driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.search("")
    count = home_page.get_product_count()
    assert count > 0, "Deberían mostrarse productos por defecto al buscar vacío."

  def test_search_nonexistent_product(self, driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.search("ProductoFalsoQueNoExiste999")
    msg = home_page.get_no_results_message()
    assert "no" in msg.lower() or "encontrado" in msg.lower(), "Debería indicar que no hay resultados."

  # --- TU APORTE - JORGE (Punto 4: Pruebas Data-Driven con @pytest.mark.parametrize) ---

  # Escenario Parametrizado A: Validaciones de campos vacíos y errores de Login
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