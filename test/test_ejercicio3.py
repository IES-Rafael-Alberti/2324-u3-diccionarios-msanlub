from src.ejercicio3 import precio
import pytest

def test_precio():
    assert precio({'platano':1.35,'manzana':0.80,'pera':0.85,'naranja':0.70},"pera") == 0.85