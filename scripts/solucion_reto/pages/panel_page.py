"""SOLUCIONARIO del reto — Page Object de la pantalla de panel de citas.

Mismo patrón que LoginPage: localizadores como atributos de clase y acciones
con nombre de negocio. Uso exclusivo del docente.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PanelPage:
    TITULO = (By.ID, "titulo-panel")
    FECHA = (By.ID, "fecha")
    BTN_AGENDAR = (By.ID, "btn-agendar")
    MENSAJE = (By.ID, "mensaje")
    ERROR = (By.ID, "error")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.url)
        return self

    def titulo(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TITULO)).text

    def agendar(self, fecha):
        campo = self.driver.find_element(*self.FECHA)
        campo.clear()
        campo.send_keys(fecha)
        self.wait.until(EC.element_to_be_clickable(self.BTN_AGENDAR)).click()

    def texto_mensaje(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MENSAJE)).text

    def texto_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR)).text
