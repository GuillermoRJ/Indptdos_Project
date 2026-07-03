"""Pruebas data-driven del login inválido con @pytest.mark.parametrize.

Una sola función genera 4 pruebas en el reporte (una por fila). Para agregar
otro caso basta con añadir una línea a la lista.
"""

import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize("usuario, clave, mensaje", [
    ("alumno@upa.edu.mx", "malisima",  "Contrasena incorrecta"),
    ("nadie@upa.edu.mx",  "Cl4v3UPA",  "Usuario no existe"),
    ("",                  "Cl4v3UPA",  "El usuario es obligatorio"),
    ("alumno@upa.edu.mx", "",          "La contrasena es obligatoria"),
])
def test_login_invalido(driver, base_url, usuario, clave, mensaje):
    login = LoginPage(driver, base_url).abrir()
    login.iniciar_sesion(usuario, clave)
    assert mensaje in login.texto_error()
