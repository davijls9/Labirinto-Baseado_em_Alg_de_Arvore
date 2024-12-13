# main.py
from src.core.gerador_labirinto import gerar_labirinto
from src.core.grafo import criar_grafo
from src.core.jogo import Jogo
from src.ui.terminal_render import mostrar_labirinto
from src.ui.gui_render import iniciar_gui
import argparse

def main():
    """
    Função principal para iniciar o jogo do labirinto.
    """
    parser = argparse.ArgumentParser(description="Jogo do Labirinto")
    parser.add_argument("--modo", choices=["terminal", "gui"], default="terminal", help="Escolha o modo de jogo: terminal ou gui")
    parser.add_argument("--linhas", type=int, default=10, help="Número de linhas do labirinto")
    parser.add_argument("--colunas", type=int, default=10, help="Número de colunas do labirinto")
    parser.add_argument("--tempo", type=int, default=60, help="Tempo limite do jogo (segundos)")

    args = parser.parse_args()

    # Gera o labirinto
    labirinto, saida = gerar_labirinto(args.linhas, args.colunas)

    # Verifica se a saída é acessível
    grafo = criar_grafo(labirinto)
    if saida not in grafo:
        print("Erro: A saída do labirinto não é acessível. Gerando novamente...")
        labirinto, saida = gerar_labirinto(args.linhas, args.colunas)
        grafo = criar_grafo(labirinto)

    # Inicializa o jogo
    jogo = Jogo(labirinto, grafo, saida, limite_tempo=args.tempo)

    if args.modo == "terminal":
        mostrar_labirinto(labirinto, {})
        jogo.executar()
    elif args.modo == "gui":
        iniciar_gui(labirinto)

if __name__ == "__main__":
    main()
