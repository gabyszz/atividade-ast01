import pytest
from estacionamento import calcular_valor_estacionamento


def test_30_minutos():
    assert calcular_valor_estacionamento(30) == 10


def test_60_minutos():
    assert calcular_valor_estacionamento(60) == 10


def test_70_minutos():
    assert calcular_valor_estacionamento(70) == 15


def test_120_minutos():
    assert calcular_valor_estacionamento(120) == 15


def test_121_minutos():
    assert calcular_valor_estacionamento(121) == 20


def test_valor_maximo():
    assert calcular_valor_estacionamento(24 * 60) == 50


def test_acima_de_24_horas():
    assert calcular_valor_estacionamento(25 * 60) == 50


def test_tempo_zero():
    with pytest.raises(ValueError):
        calcular_valor_estacionamento(0)


def test_tempo_negativo():
    with pytest.raises(ValueError):
        calcular_valor_estacionamento(-10)