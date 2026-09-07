import pytest


@pytest.fixture(scope="session")
def db_connection():
    return "Conexão Global Estabelecida"


@pytest.fixture(autouse=True)
def clean_cache():
    print("Cache limpo antes do teste")