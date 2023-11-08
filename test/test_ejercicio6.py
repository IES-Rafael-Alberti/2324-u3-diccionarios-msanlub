from src.ejercicio6 import *
import pytest

def test_nombreCorrecto():
    assert nombreCorrecto({},"Marta") == {"nombre":'Marta'}

def test_nombreNoCorrecto():
    assert nombreCorrecto({},"13") ==  None

def test_edadCorrecta():
    assert edadCorrecta({},"80") == {"edad":"80"}

def test_edadIncorrecta():
    assert edadCorrecta({},"150") == None

def test_sexoCorrecto():
    assert sexoCorrecto({},"mujer") == {"sexo":"mujer"}

def test_sexoIncorrecto():
    assert sexoCorrecto({},"452") == None

def test_telefonoCorrecto():
    assert telefonoCorrecto({},"665664663") == {"telefono":"665664663"}

def test_telefonoIncorrecto():
    assert telefonoCorrecto({},"665664663546564") == None

def test_correoCorrecto():
    assert correoIngreso({},"sdafos123dfh@sdoaifja.com") == {"correo":"sdafos123dfh@sdoaifja.com"}

def test_correoIncorrecto():
    assert correoIngreso({},"") == None