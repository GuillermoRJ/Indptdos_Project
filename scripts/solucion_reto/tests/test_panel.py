"""SOLUCIONARIO del reto — pruebas de la pantalla de panel de citas.

Cubre las tareas 1-3 del reto:
  - usa el nuevo Page Object PanelPage,
  - verifica el título del panel,
  - agenda citas con datos distintos (data-driven) y el caso de error.
"""

import pytest

from pages.panel_page import PanelPage


def test_titulo_panel(driver, panel_url):
    panel = PanelPage(driver, panel_url).abrir()
    assert panel.titulo() == "Panel de citas"


@pytest.mark.parametrize("fecha, mensaje", [
    ("2026-07-01", "Cita agendada para 2026-07-01"),
    ("2026-08-15", "Cita agendada para 2026-08-15"),
    ("2026-09-30", "Cita agendada para 2026-09-30"),
])
def test_agendar_cita_valida(driver, panel_url, fecha, mensaje):
    panel = PanelPage(driver, panel_url).abrir()
    panel.agendar(fecha)
    assert mensaje in panel.texto_mensaje()


def test_agendar_sin_fecha(driver, panel_url):
    panel = PanelPage(driver, panel_url).abrir()
    panel.agendar("")
    assert "La fecha es obligatoria" in panel.texto_error()
