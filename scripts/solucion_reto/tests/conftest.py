"""Fixtures del solucionario del reto."""

import os
import pathlib

import pytest
from selenium import webdriver


@pytest.fixture
def panel_url():
    pagina = pathlib.Path(__file__).resolve().parents[1] / "app" / "panel.html"
    return pagina.as_uri()


@pytest.fixture
def driver():
    opciones = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS"):
        opciones.add_argument("--headless=new")
        opciones.add_argument("--window-size=1920,1080")
    d = webdriver.Chrome(options=opciones)
    d.implicitly_wait(5)
    yield d
    d.quit()
