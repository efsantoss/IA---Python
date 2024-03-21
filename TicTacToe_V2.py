import random

def mostra_tabuleiro(tabuleiro):
    print("----------------")
    for linha in tabuleiro:
        print("|", linha[0], "|", linha[1], "|", linha[2], "|")
        print("----------------")

def verifica_vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
    for i in range(3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

def escolhe_marcador():
    marcador = input("Escolha o marcador (X ou O): ").upper()
    while marcador not in ['X', 'O']:
        marcador = input("Escolha o marcador (X ou O): ").upper()
    return marcador

def realiza_jogada_jogador(tabuleiro, marcador):
    linha = int(input(f"Sua vez (jogador {marcador}), escolha uma linha de 1 a 3: ")) - 1
    coluna = int(input("Escolha uma coluna de 1 a 3: ")) - 1
    if tabuleiro[linha][coluna] != " ":
        print("Posição ocupada. Tente novamente.")
        return realiza_jogada_jogador(tabuleiro, marcador)
    tabuleiro[linha][coluna] = marcador

def realiza_jogada_maquina(tabuleiro, marcador):
    print("Vez da máquina (oponente)")
    linha = random.randint(0, 2)
    coluna = random.randint(0, 2)
    while tabuleiro[linha][coluna] != " ":
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
    tabuleiro[linha][coluna] = marcador

def start_game():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    marcador_jogador = escolhe_marcador()
    marcador_maquina = "O" if marcador_jogador == "X" else "X"
    mostra_tabuleiro(tabuleiro)

    for i in range(1, 10):
        if i % 2 != 0:
            realiza_jogada_jogador(tabuleiro, marcador_jogador)
        else:
            realiza_jogada_maquina(tabuleiro, marcador_maquina)
        mostra_tabuleiro(tabuleiro)
        if verifica_vitoria(tabuleiro, marcador_jogador):
            print(f"Parabéns! Você (jogador {marcador_jogador}) ganhou!")
            return
        elif verifica_vitoria(tabuleiro, marcador_maquina):
            print("A máquina venceu! Você perdeu.")
            return
    print("Empate.")

start_game()
