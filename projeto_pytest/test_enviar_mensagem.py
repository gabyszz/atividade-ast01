from enviar_mensagem import processar_envio


def test_processar_envio(mocker):
    mock_funcao = mocker.patch("enviar_mensagem.enviar_mensagem_externa")

    mock_funcao.return_value = "Mensagem simulada"

    resultado = processar_envio("cliente@email.com", "Olá, tudo bem?")

    mock_funcao.assert_called_once_with(
        "cliente@email.com",
        "Olá, tudo bem?"
    )

    assert resultado == "Mensagem simulada"