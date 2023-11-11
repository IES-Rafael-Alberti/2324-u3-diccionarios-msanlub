from src.ejercicio1 import dameSimboloDivisa
import pytest

def test_dameSimboloDivisa():
    assert dameSimboloDivisa({'Euro':'€', 'Dollar':'$', 'Yen':'¥'},'Euro') == '€'


def test_dameSimboloDivisaQueNoExiste():
    assert dameSimboloDivisa({'Euro':'€', 'Dollar':'$', 'Yen':'¥'},'kk') == ''