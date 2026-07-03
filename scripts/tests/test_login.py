"""Prueba E2E del login exitoso usando el Page Object."""

from pages.login_page import LoginPage


def test_login_exitoso(driver, base_url):
    login = LoginPage(driver, base_url).abrir()
    login.iniciar_sesion("alumno@upa.edu.mx", "Cl4v3UPA")
    assert "Bienvenido" in login.texto_saludo()
