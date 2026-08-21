import pytest
from senha import cadastrar_senha


def test_cadastrar_senha_valida():
    # Arrange (Organizar)
    senha = "1234567890"
    esperado = True

    # Act (Agir)
    resultado = cadastrar_senha(senha)

    # Assert (Afirmar)
    assert resultado is esperado


def test_cadastrar_senha_muito_curta():
    # Arrange (Organizar)
    senha = "123"

    # Act (Agir)
    resultado = None

    # Assert (Afirmar)
    with pytest.raises(ValueError):
        cadastrar_senha(senha)


def test_mensagem_senha_muito_curta():
    # Arrange (Organizar)
    senha = "123"
    mensagem_esperada = "Senha muito curta"

    # Act (Agir)
    with pytest.raises(ValueError) as exc_info:
        cadastrar_senha(senha)

    # Assert (Afirmar)
    assert str(exc_info.value) == mensagem_esperada