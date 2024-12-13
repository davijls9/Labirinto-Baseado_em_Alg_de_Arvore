# tests/test_ia.py
from src.core.ia import IA

def test_ia_escolher_movimento():
    ia = IA()
    estado = {}  # Exemplo simplificado
    movimento = ia.escolher_movimento(estado)
    assert movimento in ["W", "A", "S", "D"]  # Movimento válido