"""Demo en vivo: la mala vs la buena forma de esperar (Semana 7, Sesión 2).

Ejecútalo directamente para mostrar en clase la diferencia entre time.sleep
y las esperas explícitas:

    python demo_esperas.py

(No es una prueba de pytest; es un script de demostración.)
"""

import pathlib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = (pathlib.Path(__file__).resolve().parent / "app" / "login.html").as_uri()


def mala_forma(driver):
    """time.sleep: espera a ciegas. Lenta si sobra tiempo, falla si falta."""
    driver.get(URL)
    driver.find_element(By.ID, "usuario").send_keys("alumno@upa.edu.mx")
    driver.find_element(By.ID, "clave").send_keys("Cl4v3UPA")
    driver.find_element(By.ID, "btn-login").click()
    time.sleep(5)  # espera fija de 5 s aunque el saludo aparezca en 0.6 s
    print("[mala]  ", driver.find_element(By.ID, "saludo").text)


def buena_forma(driver):
    """WebDriverWait: espera justo lo necesario sobre una condición concreta."""
    wait = WebDriverWait(driver, 10)
    driver.get(URL)
    driver.find_element(By.ID, "usuario").send_keys("alumno@upa.edu.mx")
    driver.find_element(By.ID, "clave").send_keys("Cl4v3UPA")
    wait.until(EC.element_to_be_clickable((By.ID, "btn-login"))).click()
    saludo = wait.until(EC.visibility_of_element_located((By.ID, "saludo")))
    print("[buena] ", saludo.text)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        t0 = time.time(); buena_forma(driver); print(f"        explícita: {time.time()-t0:.1f} s")
        t0 = time.time(); mala_forma(driver);  print(f"        sleep(5):  {time.time()-t0:.1f} s")
    finally:
        driver.quit()
