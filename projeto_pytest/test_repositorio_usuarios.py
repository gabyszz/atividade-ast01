import pytest

from repositorio_usuarios import (
    RepositorioUsuariosFake,
    GerenciadorUsuarios
)


@pytest.fixture
def gerenciador():
    repositorio = RepositorioUsuariosFake()
    return GerenciadorUsuarios(repositorio)


def test_adicionar_e_buscar_usuario(gerenciador):

    gerenciador.registrar_usuario("Maria")

    resultado = gerenciador.encontrar_usuario("Maria")

    assert resultado == "Maria"


def test_buscar_usuario_inexistente(gerenciador):

    resultado = gerenciador.encontrar_usuario("João")

    assert resultado is None