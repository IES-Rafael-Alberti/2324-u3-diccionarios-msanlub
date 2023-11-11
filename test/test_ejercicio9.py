from src.ejercicio9 import *
import pytest

def test_añadirNuevaFactura():
    assert añadirNuevaFactura({},"4:40") == {"4":"40"}

