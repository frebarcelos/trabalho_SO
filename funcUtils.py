import os
def limpar_terminal():    
    os.system('cls' if os.name == 'nt' else 'clear')
def adiciona_zero_esquerda(numero):
    return f"0{numero}" if numero < 10 else str(numero)