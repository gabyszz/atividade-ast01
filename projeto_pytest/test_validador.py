import pytest
from validador import validar_acesso

def test_acesso_permitido():
    resultado = validar_acesso(20, True)
    assert resultado == "Acesso Permitido"

def test_menor_de_idade():
    resultado = validar_acesso(15, False)
    assert resultado == "Acesso Negado: Menor de Idade"

def test_acesso_vip():
    resultado = validar_acesso(20, False, vip=True)
    assert resultado == "Acesso VIP Liberado"

def test_comprar_ingressos():
    resultado = validar_acesso(20, False)
    assert resultado == "Comprar Ingressos"

def test_idade_invalida():
    with pytest.raises(ValueError, match="Idade inválida"):
        validar_acesso(-1, False)