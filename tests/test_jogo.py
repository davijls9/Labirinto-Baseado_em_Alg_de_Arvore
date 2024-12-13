# tests/test_jogo.py
from src.core.jogo import Jogo
from src.core.gerador_labirinto import gerar_labirinto
from src.core.grafo import criar_grafo

def test_jogo_fluxo():
    labirinto, saida = gerar_labirinto(5, 5)
    grafo = criar_grafo(labirinto)
    jogo = Jogo(labirinto, grafo, saida, limite_tempo=10)

    assert jogo.posicao == (1, 1)
    assert not jogo.mover("A")  # Movimento inválido
    assert jogo.mover("S")  # Movimento válido
    assert jogo.posicao != (1, 1)