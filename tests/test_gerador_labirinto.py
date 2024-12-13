# tests/test_gerador_labirinto.py
import pytest
from src.core.gerador_labirinto import gerar_labirinto

def test_gerar_labirinto():
    labirinto, saida = gerar_labirinto(10, 10)
    assert len(labirinto) == 10
    assert len(labirinto[0]) == 10
    assert labirinto[1][1] == " "  # Ponto inicial
    assert labirinto[saida[0]][saida[1]] == "E"  # Saída está correta