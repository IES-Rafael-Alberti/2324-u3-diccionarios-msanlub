from src.ejercicio4 import convertirFechaEnLista
import pytest

def test_convertirFechaEnLista():
    assert convertirFechaEnLista("24/03/1992") == ["24","03","1992"]