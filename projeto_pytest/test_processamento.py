import os
import pytest


@pytest.fixture
def ambiente_testing():
    # Setup
    os.environ["APP_ENV"] = "testing"

    banco_falso = ["item1", "item2"]

    # Entrega o banco para o teste
    yield banco_falso

    # Teardown
    if "APP_ENV" in os.environ:
        del os.environ["APP_ENV"]


def test_processamento_de_dados(ambiente_testing):
    # Execução
    ambiente_testing.append("item3")

    # Asserções
    assert os.environ["APP_ENV"] == "testing"
    assert len(ambiente_testing) == 3