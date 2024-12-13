# tests/test_estado.py
from src.utils.estado import salvar_estado, carregar_estado
import os
import json

def test_salvar_carregar_estado(tmp_path):
    labirinto = [["#", "#"], [" ", "E"]]
    posicao = (1, 1)
    visitas = {}
    arquivo = tmp_path / "estado.json"

    salvar_estado(labirinto, posicao, visitas, arquivo)
    assert os.path.exists(arquivo)

    estado = carregar_estado(arquivo)
    assert estado["posicao"] == posicao
    assert estado["labirinto"] == labirinto