import os
import pytest


@pytest.fixture
def log_file():
    # Setup
    caminho = "test_log.txt"

    # Entrega o recurso para o teste
    yield caminho

    # Teardown
    if os.path.exists(caminho):
        os.remove(caminho)


def test_escrita_log(log_file):
    with open(log_file, "w") as arquivo:
        arquivo.write("Teste de log")

    assert os.path.exists(log_file)