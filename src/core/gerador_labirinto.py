# src/core/gerador_labirinto.py
import random

def gerar_labirinto(linhas, colunas):
    """
    Gera o labirinto com base no número de linhas e colunas fornecidos.
    """
    labirinto = [["█" for _ in range(colunas)] for _ in range(linhas)]

    # Gera um caminho inicial
    caminho = [(1, 1)]
    labirinto[1][1] = "S"  # Início do jogador

    while caminho:
        x, y = caminho[-1]
        vizinhos = [
            (x - 2, y, x - 1, y),
            (x + 2, y, x + 1, y),
            (x, y - 2, x, y - 1),
            (x, y + 2, x, y + 1),
        ]
        random.shuffle(vizinhos)
        for nx, ny, wx, wy in vizinhos:
            if 1 <= nx < linhas - 1 and 1 <= ny < colunas - 1 and labirinto[nx][ny] == "█":
                labirinto[nx][ny] = "░"
                labirinto[wx][wy] = "░"
                caminho.append((nx, ny))
                break
        else:
            caminho.pop()

    # Define uma saída alcançável
    for x in range(linhas - 2, 0, -1):
        for y in range(colunas - 2, 0, -1):
            if labirinto[x][y] == "░":
                labirinto[x][y] = "E"
                return labirinto, (x, y)

    return labirinto, (linhas - 2, colunas - 2)  # Caso excepcional