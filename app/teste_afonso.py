from app import app

def test_saude_tem_versao():
    dados = app.test_client().get("/saude").get_json()
    assert "versao" in dados