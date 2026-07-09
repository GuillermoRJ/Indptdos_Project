import pytest
from ..pages.login_page import LoginPage
from ..pages.home_page import HomePage


class TestEcommerceE2E:

    # 1. Caso Válido: Inicio de sesión exitoso
    def test_login_success(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(
            "guillermo@test.com",
            "$2b$10$K6kLPHIl5hO6XvIHWt3hwO1tFtzptxF76ee1YaIi.AUxINMjRM.Fu",
        )

        home_page = HomePage(driver)
        assert driver.current_url == home_page.URL or "dashboard" in driver.current_url

    # 2. Caso de Error: Inicio de sesión con credenciales inválidas
    def test_login_invalid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("no@test.com", "no")

        error_msg = login_page.get_error_message()
        assert len(error_msg) > 0, "Debería mostrarse un mensaje de error."

    # 3. Caso Frontera (Boundary): Búsqueda con string vacío
    def test_search_empty_string(self, driver):
        home_page = HomePage(driver)
        home_page.load()
        home_page.search("")

        count = home_page.get_product_count()
        assert count > 0, "Deberían mostrarse productos por defecto al buscar vacío"

    # 4. Caso Data-Driven (Múltiples Casos Válidos en uno): Buscar productos que existen
    @pytest.mark.parametrize(
        "producto, cantidad_esperada",
        [
            ("Small Aluminum Fish", 18),
            ("Refined Granite Towels", 36),
            ("Bespoke Cotton Table", 41),
        ],
    )
    def test_search_existing_products_data_driven(
        self, driver, producto, cantidad_esperada
    ):
        home_page = HomePage(driver)
        home_page.load()
        home_page.search(producto)

        count = home_page.get_product_count()
        assert count >= cantidad_esperada, f"Fallo al encontrar {producto}"

    # 5. Caso de Error: Búsqueda de un producto inexistente
    def test_search_nonexistent_product(self, driver):
        home_page = HomePage(driver)
        home_page.load()
        home_page.search("ProductoF")

        msg = home_page.get_no_results_message()
        assert (
            "no" in msg.lower() or "encontrado" in msg.lower()
        ), "Debería indicar que no hay resultados."
