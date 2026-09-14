def calcular_desconto(valor_original, percentual_desconto):
    if percentual_desconto < 0 or percentual_desconto > 100:
        raise ValueError("O desconto deve estar entre 0 e 100.")

    desconto = valor_original * (percentual_desconto / 100)
    valor_final = valor_original - desconto

    return max(valor_final, 0)