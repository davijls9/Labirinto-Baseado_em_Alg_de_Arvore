# src/core/ia.py
import heapq
import logging
import random
from collections import defaultdict

# Configuração de logging
logging.basicConfig(
    filename="ia_debug.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class IA:
    def __init__(self):
        self.caminho = []
        self.mapa_conhecido = set()
        self.vizinhos_conhecidos = {}
        self.q_table = defaultdict(lambda: defaultdict(float))  # Para aprendizado Q-Learning
        self.direcoes = {"W": (-1, 0), "S": (1, 0), "A": (0, -1), "D": (0, 1)}
        self.ultima_direcao = None
        self.epsilon = 0.1  # Probabilidade de exploração
        self.alpha = 0.1  # Taxa de aprendizado
        self.gamma = 0.9  # Fator de desconto
        logging.info("IA inicializada.")

    def atualizar_mapa(self, posicao, mapa_atual):
        """
        Atualiza o mapa conhecido com a posição atual e seus vizinhos acessíveis.
        """
        logging.debug(f"Atualizando mapa na posição: {posicao}")
        if isinstance(mapa_atual, dict):
            for vizinho in mapa_atual.get(posicao, []):
                self.mapa_conhecido.add(vizinho)
                self.vizinhos_conhecidos.setdefault(posicao, []).append(vizinho)
                self.vizinhos_conhecidos.setdefault(vizinho, []).append(posicao)

        elif isinstance(mapa_atual, list):
            if posicao not in self.mapa_conhecido:
                self.mapa_conhecido.add(posicao)
                self.vizinhos_conhecidos[posicao] = []

            for dx, dy in self.direcoes.values():
                vizinho = (posicao[0] + dx, posicao[1] + dy)
                if 0 <= vizinho[0] < len(mapa_atual) and 0 <= vizinho[1] < len(mapa_atual[0]):
                    if mapa_atual[vizinho[0]][vizinho[1]] != "█":
                        self.mapa_conhecido.add(vizinho)
                        self.vizinhos_conhecidos.setdefault(posicao, []).append(vizinho)
                        self.vizinhos_conhecidos.setdefault(vizinho, []).append(posicao)

    def calcular_caminho(self, inicio, destino):
        """
        Usa o algoritmo A* para calcular o caminho mais curto no mapa conhecido.
        Retorna uma lista de posições que compõem o caminho.
        """
        def heuristica(no1, no2):
            return abs(no1[0] - no2[0]) + abs(no1[1] - no2[1])

        logging.debug(f"Calculando caminho de {inicio} para {destino}.")
        open_set = [(0, inicio)]
        came_from = {}
        g_score = defaultdict(lambda: float('inf'))
        g_score[inicio] = 0
        f_score = defaultdict(lambda: float('inf'))
        f_score[inicio] = heuristica(inicio, destino)

        while open_set:
            _, no_atual = heapq.heappop(open_set)
            if no_atual == destino:
                caminho = []
                while no_atual in came_from:
                    caminho.append(no_atual)
                    no_atual = came_from[no_atual]
                caminho.reverse()
                logging.debug(f"Caminho encontrado: {caminho}")
                return caminho

            for vizinho in self.vizinhos_conhecidos.get(no_atual, []):
                tentative_g_score = g_score[no_atual] + 1
                if tentative_g_score < g_score[vizinho]:
                    came_from[vizinho] = no_atual
                    g_score[vizinho] = tentative_g_score
                    f_score[vizinho] = tentative_g_score + heuristica(vizinho, destino)
                    heapq.heappush(open_set, (f_score[vizinho], vizinho))

        logging.debug("Caminho não encontrado.")
        return []

    def escolher_movimento(self, posicao_atual, mapa_atual):
        """
        Retorna o próximo movimento com base no mapa conhecido e na Q-Table.
        """
        logging.debug(f"Escolhendo movimento a partir da posição {posicao_atual}.")
        
        if not isinstance(posicao_atual, tuple) or len(posicao_atual) != 2:
            logging.error(f"Formato inválido de posicao_atual: {posicao_atual}")
            return random.choice(list(self.direcoes.keys()))  # Movimento padrão aleatório

        self.atualizar_mapa(posicao_atual, mapa_atual)

        if random.random() < self.epsilon:
            # Exploração: escolhe um movimento aleatório
            movimento = random.choice(list(self.direcoes.keys()))
        else:
            # Exploração: escolhe o movimento com maior recompensa esperada
            movimento = max(self.direcoes.keys(), key=lambda d: self.q_table[posicao_atual][d])

        dx, dy = self.direcoes[movimento]
        nova_posicao = (posicao_atual[0] + dx, posicao_atual[1] + dy)

        # Atualização da Q-Table
        recompensa = 1 if nova_posicao not in self.mapa_conhecido else -1
        max_q = max(self.q_table[nova_posicao].values(), default=0)
        self.q_table[posicao_atual][movimento] += self.alpha * (
            recompensa + self.gamma * max_q - self.q_table[posicao_atual][movimento]
        )

        logging.debug(f"Movimento escolhido: {movimento}")
        return movimento
