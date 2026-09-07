def test_conexao_1(db_connection):
    assert db_connection == "Conexão Global Estabelecida"


def test_conexao_2(db_connection):
    assert db_connection == "Conexão Global Estabelecida"