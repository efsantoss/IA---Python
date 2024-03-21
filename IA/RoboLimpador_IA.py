import random
import time

## Ambiente 3x3
LINHAS = 3
COLUNAS = 3
AGENTE = "A"
LIMPO = "limpo"
SUJO = "sujo"

## Posição inicial do aspirador
linha_atual = random.randint(0, LINHAS-1)
coluna_atual = random.randint(0, COLUNAS-1)

## Ambiente inicial
ambiente = [[SUJO for _ in range(COLUNAS)] for _ in range(LINHAS)]

## Funcao pra mostrar o programa rodando
def mostrar_na_tela(ambiente):
    for linha in ambiente:
        print(" ".join(linha))
    print("\n")

## Funcao pra simula o movimento e a limpeza do aspirador.
def aspirar(ambiente):
    global linha_atual, coluna_atual
    while True:
        ## Aki limpa a sala atual
        ambiente[linha_atual][coluna_atual] = LIMPO
        mostrar_na_tela(ambiente)
        time.sleep(0.5)

        ## Aki move o aspirador
        movimento = random.randint(0, 3)
        if movimento == 0 and linha_atual > 0:
            ## Mover para cima
            linha_atual -= 1
        elif movimento == 1 and linha_atual < LINHAS-1:
            ## Mover para baixo
            linha_atual += 1
        elif movimento == 2 and coluna_atual > 0:
            ## Mover pro lado esquerdo
            coluna_atual -= 1
        elif movimento == 3 and coluna_atual < COLUNAS-1:
            ## Mover pro lado direito
            coluna_atual += 1

        ## Aki Veifica se todas as salas sao limpas
        if all(sala == LIMPO for linha in ambiente for sala in linha):
            print("Todas as salas estão limpas!")
            break

        ## Aki se tiver sujo vai pra sala que esta suja
        if ambiente[linha_atual][coluna_atual] == SUJO:
            continue

        ## Aki se tiver td limpo para o programa
        if all(sala == LIMPO for linha in ambiente for sala in linha):
            print("Todas as salas estão limpas!")
            break

aspirar(ambiente)
