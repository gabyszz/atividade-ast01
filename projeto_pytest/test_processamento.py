from unittest.mock import Mock, call

from processamento import ProcessadorDeAcoes


def test_executar_processo():

    processador = ProcessadorDeAcoes()

    chamadas = Mock()

    def validar(dados):
        chamadas.validar(dados)
        return True

    def salvar(dados):
        chamadas.salvar(dados)
        return True

    processador.validar_dados = validar
    processador.salvar_dados = salvar

    dados = {
        "nome": "Maria",
        "idade": 25
    }

    resultado = processador.executar_processo(dados)

    assert resultado == "Processo executado com sucesso"

    roteiro_esperado = [
        call.validar(dados),
        call.salvar(dados)
    ]

    chamadas.assert_has_calls(
        roteiro_esperado,
        any_order=False
    )