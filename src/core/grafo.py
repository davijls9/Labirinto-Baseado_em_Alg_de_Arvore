# src/core/grafo.py
def criar_grafo(labirinto):
    """
    Cria um grafo baseado no labirinto.
    """
    grafo = {}
    linhas, colunas = len(labirinto), len(labirinto[0])
    for x in range(1, linhas - 1):
        for y in range(1, colunas - 1):
            if labirinto[x][y] in (" ", "E"):
                conexoes = []
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if labirinto[nx][ny] in (" ", "E"):
                        conexoes.append((nx, ny))
                grafo[(x, y)] = conexoes
    return grafo