from src.ejercicio7 import *
import pytest

def test_ingresoEnLista():
    assert ingresoEnLista({},"pan","1,30") == {"pan":"1,30"}

def test_precioTotal():
    assert precioTotal({"pan":1.30},1.30) == 1.30