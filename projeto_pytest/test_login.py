"""Módulo de testes automatizados para a funcionalidade de login."""


def realizar_login(
    usuario: bool, senha: str | None, forcar_erro: bool
) -> bool:
    """Executa a lógica simulada de login."""
    resultado_login = False

    if usuario:
        if senha is not None:
            if not forcar_erro:
                print(
                    "Iniciando o processo de login no sistema com credenciais "
                    "validas e aguardando o tempo de resposta do servidor..."
                )
                resultado_login = True
            else:
                print("Erro forcado")
        else:
            print("Senha vazia")
    else:
        print("Usuario invalido")

    return resultado_login


def test_verificar_login_valido() -> None:
    """Valida se o login é bem-sucedido com credenciais corretas."""
    token_sessao = "abc123xyz"  # noqa: F841
    assert realizar_login(True, "123456", False) is True
