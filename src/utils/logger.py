# src/utils/logger.py
import logging

def configurar_logger(nome_arquivo):
    """
    Configura o logger para salvar mensagens em arquivo.
    """
    logger = logging.getLogger("labirinto_logger")
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(nome_arquivo)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger