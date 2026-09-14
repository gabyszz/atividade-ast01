import math


def calcular_valor_estacionamento(tempo_em_minutos):
    if tempo_em_minutos <= 0:
        raise ValueError("O tempo deve ser maior que zero.")

    if tempo_em_minutos <= 60:
        return 10

    horas_adicionais = math.ceil((tempo_em_minutos - 60) / 60)

    valor = 10 + (horas_adicionais * 5)

    return min(valor, 50)