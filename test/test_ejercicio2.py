from src.ejercicio2 import *

def test_guardarDatosEnDiccionario():
    assert guardarDatosEnDiccionario("Marta","31","Jaen","666666666") == {'nombre': 'Marta','edad': '31','direccion': 'Jaen','telefono': '666666666'}