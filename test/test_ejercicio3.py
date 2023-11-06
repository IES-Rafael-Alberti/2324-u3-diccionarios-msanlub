from src.ejercicio3 import precioTotal
import pytest

def test_precioTotal():
    assert precioTotal({'platano':'1.35','manzana':'0.80','pera':'0.85','naranja':'0.70'},"peras", 3.0) == 2.55