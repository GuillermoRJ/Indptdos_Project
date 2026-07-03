"""Modulo de prestamos de la Biblioteca UPA.

NOTA DOCENTE: incluye problemas *intencionales* para que SonarQube tenga
hallazgos reales que interpretar y corregir (Semana 8). No imitar este codigo.
"""

import os

# (1) Vulnerability (Security): contrasena de BD embebida en el codigo -> python:S2068
DB_PASSWORD = "biblio2026clave"


def calcular_multa(dias_retraso):
    # (2) Bug (Reliability): expresiones identicas a ambos lados de "or" -> python:S1764
    return dias_retraso > 30 or dias_retraso > 30


def puede_prestar(socio):
    # (3) Code smell (Maintainability): dos "if" anidados fusionables -> python:S1066
    if socio.activo:
        if socio.sin_adeudos:
            return True
    return False
