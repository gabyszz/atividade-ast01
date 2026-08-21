from idade import pode_dirigir


def test_pode_dirigir_maior_de_idade():
    # Arrange (Organizar)
    idade = 20
    esperado = True

    # Act (Agir)
    resultado = pode_dirigir(idade)

    # Assert (Afirmar)
    assert resultado is esperado


def test_nao_pode_dirigir_menor_de_idade():
    # Arrange (Organizar)
    idade = 16
    esperado = False

    # Act (Agir)
    resultado = pode_dirigir(idade)

    # Assert (Afirmar)
    assert resultado is esperado