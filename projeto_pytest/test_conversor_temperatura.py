import pytest
from conversor_temperatura import (
    celsius_para_fahrenheit,
    fahrenheit_para_celsius
)


def test_zero_celsius():
    assert celsius_para_fahrenheit(0) == 32


def test_cem_celsius():
    assert celsius_para_fahrenheit(100) == 212


def test_trinta_e_dois_fahrenheit():
    assert fahrenheit_para_celsius(32) == 0


def test_duzentos_e_doze_fahrenheit():
    assert fahrenheit_para_celsius(212) == 100


def test_celsius_nao_numerico():
    with pytest.raises(TypeError):
        celsius_para_fahrenheit("25")


def test_fahrenheit_nao_numerico():
    with pytest.raises(TypeError):
        fahrenheit_para_celsius("77")