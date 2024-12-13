# src/ui/gui_render.py
import pygame

def iniciar_gui(labirinto):
    """
    Inicia a interface gráfica do labirinto usando pygame.
    """
    pygame.init()
    tamanho_celula = 20
    linhas, colunas = len(labirinto), len(labirinto[0])
    tela = pygame.display.set_mode((colunas * tamanho_celula, linhas * tamanho_celula))
    pygame.display.set_caption("Labirinto GUI")

    cores = {
        "#": (255, 0, 0),    # Vermelho para paredes
        " ": (0, 255, 0),    # Verde para caminhos
        "E": (255, 255, 0),  # Amarelo para a saída
    }

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        for i, linha in enumerate(labirinto):
            for j, celula in enumerate(linha):
                cor = cores.get(celula, (0, 0, 0))  # Preto para qualquer outro símbolo
                pygame.draw.rect(
                    tela, cor, pygame.Rect(j * tamanho_celula, i * tamanho_celula, tamanho_celula, tamanho_celula)
                )

        pygame.display.flip()

    pygame.quit()