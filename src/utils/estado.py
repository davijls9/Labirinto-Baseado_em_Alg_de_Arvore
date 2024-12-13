# src/utils/estado.py
import json

def salvar_estado(labirinto, posicao, visitas, arquivo="estado.json"):
    """
    Salva o estado atual do jogo em um arquivo JSON.
    """
    estado = {
        "labirinto": labirinto,
        "posicao": posicao,
        "visitas": visitas,
    }
    with open(arquivo, "w") as f:
        json.dump(estado, f)

def carregar_estado(arquivo="estado.json"):
    """
    Carrega o estado do jogo a partir de um arquivo JSON.
    """
    with open(arquivo, "r") as f:
        return json.load(f)