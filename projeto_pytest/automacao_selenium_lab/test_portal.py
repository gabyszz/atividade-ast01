import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def navegador():

    navegador = webdriver.Chrome()

    caminho_html = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "portal.html")
    )

    navegador.get("file://" + caminho_html)

    yield navegador

    navegador.quit()


def test_preencher_formulario(navegador):

    assert navegador.title == "Portal do Colaborador"

    nome = navegador.find_element(By.ID, "nome")
    nome.send_keys("Gabrielly Grasso")

    email = navegador.find_element(By.ID, "email")
    email.send_keys("gabrielly@empresa.com")

    botao_enviar = navegador.find_element(By.ID, "enviar")
    botao_enviar.click()

    mensagem = navegador.find_element(By.ID, "mensagem-sucesso")

    assert mensagem.is_displayed()
    assert mensagem.text == "Dados enviados com sucesso!"


def test_acoes_avancadas_mouse(navegador):

    botao_duplo_clique = navegador.find_element(
        By.ID, "duplo-clique"
    )

    ActionChains(navegador).double_click(
        botao_duplo_clique
    ).perform()

    assert botao_duplo_clique.text == "Autorizado!"

    botao_clique_direito = navegador.find_element(
        By.ID, "clique-direito"
    )

    ActionChains(navegador).context_click(
        botao_clique_direito
    ).perform()

    assert botao_clique_direito.text == "Menu Aberto!"


def test_acoes_teclado(navegador):

    campo_texto = navegador.find_element(
        By.ID, "observacoes"
    )

    campo_texto.click()

    ActionChains(navegador).key_down(
        Keys.CONTROL
    ).send_keys("a").key_up(
        Keys.CONTROL
    ).send_keys(
        Keys.BACKSPACE
    ).perform()

    campo_texto.send_keys(
        "Teste automatizado finalizado."
    )

    assert campo_texto.get_attribute(
        "value"
    ) == "Teste automatizado finalizado."