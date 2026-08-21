def calcular_desconto(valor, percentual):
    if percentual > 50:
        percentual = 50

    desconto = valor * (percentual / 100)
    return valor - desconto