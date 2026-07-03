# Selenium avanzado — proyecto de clase (Semana 7, Sesión 2)

Proyecto **ejecutable y autocontenido** que materializa el código de la
presentación `semana07_s2_simple`: esperas explícitas, Page Object Model (POM)
e integración con pytest. No necesita internet ni un servidor real: incluye una
página de demo local (`app/login.html`).

## Estructura

```
semana07_s2_selenium/
  app/
    login.html              # página de demo (login con validación asíncrona)
  pages/
    login_page.py           # Page Object de la pantalla de login
  tests/
    conftest.py             # fixtures (driver, base_url) y hook de captura
    test_login.py           # login exitoso
    test_login_invalido.py  # data-driven con @parametrize (4 casos)
  demo_esperas.py           # demo en vivo: time.sleep vs WebDriverWait
  requirements.txt
  pytest.ini
  .github/workflows/pruebas.yml
```

## Requisitos

- Python 3.10+
- Google Chrome instalado (Selenium 4 descarga el driver automáticamente con
  *Selenium Manager*; no hace falta instalar chromedriver a mano).

## Instalación

```bash
cd scripts/semana07_s2_selenium
python -m venv .venv
# Windows:  .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar las pruebas

```bash
pytest                 # todas (abre Chrome y corre 5 pruebas)
pytest -v              # con detalle
pytest tests/test_login.py
pytest tests/test_login.py::test_login_exitoso
pytest -x              # detenerse en el primer fallo
HEADLESS=1 pytest      # sin ventana (Linux/Mac); en Windows: set HEADLESS=1
```

Reporte HTML navegable:

```bash
pytest --html=reporte.html --self-contained-html
```

## Demo en vivo (esperas)

```bash
python demo_esperas.py
```

Muestra que la espera explícita resuelve en ~0.6 s lo que `time.sleep(5)`
tarda 5 s, ilustrando por qué `sleep` produce pruebas lentas y *flaky*.

## Credenciales de la demo

- Usuario válido: `alumno@upa.edu.mx`
- Contraseña válida: `Cl4v3UPA`

Cualquier otra combinación dispara uno de los mensajes de error que comprueban
las pruebas data-driven.
