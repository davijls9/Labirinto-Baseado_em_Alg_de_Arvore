# src/core/jogo.py
import time
import threading
from src.ui.terminal_render import mostrar_labirinto
from src.core.gerador_labirinto import gerar_labirinto
from src.core.grafo import criar_grafo
from src.core.ia import IA

class Jogo:
    def __init__(self, labirinto, grafo, saida, limite_tempo=60):
        self.labirinto = labirinto
        self.grafo = grafo
        self.saida = saida
        self.posicao = (1, 1)
        self.visitas = {}
        self.tempo_inicial = time.time()
        self.limite_tempo = limite_tempo
        self.pontuacao = 1000  # Pontuação inicial
        self.ia = IA()
        self.ia_rodando = False

    def mover(self, comando):
        movimentos = {
            "W": (-1, 0),
            "S": (1, 0),
            "A": (0, -1),
            "D": (0, 1),
        }
        if comando in movimentos:
            dx, dy = movimentos[comando]
            nx, ny = self.posicao[0] + dx, self.posicao[1] + dy

            if self.labirinto[nx][ny] in ("░", "E"):
                revisitado = self.visitas.get(self.posicao, 0) > 0
                self.visitas[self.posicao] = self.visitas.get(self.posicao, 0) + 1
                self.labirinto[self.posicao[0]][self.posicao[1]] = "░"  # Marca o caminho
                self.posicao = (nx, ny)
                self.labirinto[nx][ny] = "S"  # Atualiza posição do jogador

                # Atualiza pontuação
                if revisitado:
                    self.pontuacao -= 50  # Penalidade maior para locais revisitados
                else:
                    self.pontuacao -= 5

                if self.posicao == self.saida:
                    return True

        return False

    def executar(self):
        while time.time() - self.tempo_inicial < self.limite_tempo:
            mostrar_labirinto(self.labirinto, self.visitas)
            print(f"Pontuação: {self.pontuacao}")
            comando = input("Movimento (W/A/S/D/N/Q/I): ").strip().upper()
            if comando == "Q":
                print("Jogo encerrado!")
                break
            if comando == "N":
                print("Iniciando um novo jogo...")
                self.__init__(*self._gerar_novo_jogo())
                continue
            if comando == "I":
                print("IA assumindo controle... Pressione qualquer tecla para interromper.")
                self.ia_rodando = True
                ia_thread = threading.Thread(target=self._executar_ia)
                ia_thread.start()
                input()  # Aguarda interrupção
                self.ia_rodando = False
                ia_thread.join()
                continue
            if self.mover(comando):
                mostrar_labirinto(self.labirinto, self.visitas)
                print(f"Parabéns! Você encontrou a saída! Pontuação final: {self.pontuacao}")
                break
        else:
            print("Tempo limite atingido! Você perdeu.")

    def _executar_ia(self):
        while self.ia_rodando and not self.mover(self.ia.escolher_movimento(self.grafo, self.posicao)):
            mostrar_labirinto(self.labirinto, self.visitas)
            time.sleep(0.5)
        if self.ia_rodando and self.posicao == self.saida:
            print(f"IA encontrou a saída! Pontuação final: {self.pontuacao}")
            self.ia_rodando = False

    def _gerar_novo_jogo(self):
        while True:
            try:
                linhas, colunas = map(int, input("Digite o tamanho do labirinto (linhas colunas): ").split())
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira dois números separados por espaço.")
        labirinto, saida = gerar_labirinto(linhas, colunas)
        grafo = criar_grafo(labirinto)
        return labirinto, grafo, saida, self.limite_tempo