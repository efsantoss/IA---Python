def mostra_tabuleiro(tabuleiro):

    print("----------------")

    for linha in tabuleiro:

        print("|", linha [0], "|", linha [1], "|", linha [2], "|")
        print("---------------")

def verifica_vitoria(tabuleiro, jogador):

    for i in range(0,3):

        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
        
    for i in range(0,3):

        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
        
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    
    return False 
    




def start_game():

    tabuleiro = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]

    ]

    jogadores = ["X","O"]
    jogador_atual = jogadores [0]

    mostra_tabuleiro(tabuleiro)

    for i in range(1,10):

        linha = int(input(f"Jogador {jogador_atual} escolha uma linha de 1-3: ")) -1
        coluna = int(input(f"Jogador {jogador_atual} escolha uma coluna de 1-3: ")) -1

        if tabuleiro[linha][coluna] != " ":
            print(f"Posição ocupada.")
            linha = int(input(f"Jogador {jogador_atual} escolha uma linha de 1-3: ")) -1
            coluna = int(input(f"Jogador {jogador_atual} escolha uma coluna de 1-3: ")) -1

        tabuleiro[linha][coluna] = jogador_atual
        mostra_tabuleiro(tabuleiro)

        if verifica_vitoria(tabuleiro, jogador_atual):

            print(f"VOCE {jogador_atual} GANHOU,  LINDO !!!")
            return
        
        jogador_atual = jogadores[i % 2]
    
    print("Empate.")

start_game()