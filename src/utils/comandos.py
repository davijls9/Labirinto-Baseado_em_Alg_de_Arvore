# src/utils/comandos.py
def carregar_comando():
    """
    Lê e valida o comando do usuário.
    """
    comando = input("Digite seu comando (W/A/S/D/Q): ").strip().upper()
    if comando in ["W", "A", "S", "D", "Q"]:
        return comando
    print("Comando inválido!")
    return None