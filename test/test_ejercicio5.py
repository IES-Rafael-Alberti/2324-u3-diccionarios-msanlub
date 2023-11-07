from src.ejercicio5 import totalCreditos
import pytest

def test_totalCreditos():
    assert totalCreditos({'Matemáticas':6,'Física':4,'Química':5}) == 15