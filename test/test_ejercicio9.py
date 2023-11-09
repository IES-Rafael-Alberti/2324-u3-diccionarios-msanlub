from src.ejercicio9 import *
import pytest

def test_añadirNuevaFactura():
    assert añadirNuevaFactura({},"4:40") == {"4":"40"}

def test_procesoPagarFactura():
    assert procesoPagarFactura({"4":"40"},"4") == "La factura se ha pagado."