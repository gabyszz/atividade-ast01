import pytest
from calculadora_desconto import calcular_desconto


def test_desconto_10_porcento():
    resultado = calcular_desconto(100, 10)

    assert resultado == 90


def test_desconto_20_porcento():
    resultado = calcular_desconto(200, 20)

    assert resultado == 160


def test_desconto_zero():
    resultado = calcular_desconto(100, 0)

    assert resultado == 100


def test_desconto_maior_que_100():
    with pytest.raises(ValueError):
        calcular_desconto(100, 101)


def test_desconto_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(100, -10)


def test_valor_final_nao_negativo():
    resultado = calcular_desconto(50, 100)

    assert resultado == 0