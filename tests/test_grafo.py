# tests/test_grafo.py
from src.core.grafo import criar_grafo

def test_criar_grafo():
    labirinto = [
        ["#", "#", "#"],
        ["#", " ", "E"],
        ["#", "#", "#"],
    ]
    grafo = criar_grafo(labirinto)
    assert (1, 1) in grafo
    assert (1, 2) in grafo[(1, 1)]  # Conexão com saída