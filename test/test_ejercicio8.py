from src.ejercicio8 import *
import pytest

def test_ingresarEnDiccionario():
    assert ingresarEnDiccionario({},"hola:hello") == {'hola':'hello'}

def test_traducir():
    assert traducir('hola nat',{'hola':'hello','nat':'natalia'}) == "hello natalia "