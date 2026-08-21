import pytest
from carrinho import CarrinhoDeCompras


def test_adicionar_item():
    # Arrange (Organizar)
    carrinho = CarrinhoDeCompras()
    item = "Notebook"

    # Act (Agir)
    carrinho.adicionar_item(item)

    # Assert (Afirmar)
    assert item in carrinho.listar_itens()


def test_remover_item():
    # Arrange (Organizar)
    carrinho = CarrinhoDeCompras()
    item = "Notebook"
    carrinho.adicionar_item(item)

    # Act (Agir)
    carrinho.remover_item(item)

    # Assert (Afirmar)
    assert item not in carrinho.listar_itens()


def test_remover_item_inexistente():
    # Arrange (Organizar)
    carrinho = CarrinhoDeCompras()
    item = "Celular"

    # Act (Agir)
    with pytest.raises(ValueError):
        carrinho.remover_item(item)

    # Assert (Afirmar)
    assert item not in carrinho.listar_itens()