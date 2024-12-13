# Atualiza o renderizador no terminal para adicionar jogador e legenda
# src/ui/terminal_render.py
import os

def aplicar_cor(simbolo, visitas):
    """
    Aplica cores para melhor visualização no terminal.
    """
    if simbolo == "E":
        return f"\033[93m{simbolo}\033[0m"  # Amarelo para a saída
    elif simbolo == "S":
        return f"\033[94m{simbolo}\033[0m"  # Azul para o jogador
    elif simbolo == "░":
        if visitas > 1:
            return f"\033[91m{simbolo}\033[0m"  # Vermelho para locais revisitados
        return f"\033[92m{simbolo}\033[0m"  # Verde para caminho normal
    elif simbolo == "█":
        return f"\033[97m{simbolo}\033[0m"  # Branco para paredes
    return simbolo

def mostrar_labirinto(labirinto, visitas):
    """
    Renderiza o labirinto no terminal com legenda.
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("Legenda:")
    print("  \033[92m░\033[0m - Caminho | \033[97m█\033[0m - Parede | \033[93mE\033[0m - Saída | \033[94mS\033[0m - Jogador | \033[91m░\033[0m - Revisitado")
    print("  W - Mover para cima | S - Mover para baixo | A - Mover para a esquerda | D - Mover para a direita")
    print("  N - Novo jogo | Q - Sair | I - IA joga (Pressione qualquer tecla para interromper a IA)\n")
    for i, linha in enumerate(labirinto):
        linha_colorida = "".join(aplicar_cor(simbolo, visitas.get((i, j), 0)) for j, simbolo in enumerate(linha))
        print(linha_colorida)
    print()