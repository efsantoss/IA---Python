# Função para separar números pares e ímpares
def separar_pares_impares(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

# Função principal
def main():
    numeros = []
    for i in range(20):
        num = int(input("Digite o {}º número inteiro: ".format(i+1)))
        numeros.append(num)
    
    pares, impares = separar_pares_impares(numeros)
    
    print("Números PARES:", pares)
    print("Tamanho dos números PARES:", len(pares))
    
    print("\nNúmeros ÍMPARES:", impares)
    print("Tamanho dos números ÍMPARES:", len(impares))

if __name__ == "__main__":
    main()

#######################################################################################
    

# Função para remover números negativos de uma lista
def remover_negativos(lista):
    return [num for num in lista if num >= 0]

# Função principal
def main():
    lista = []
    for i in range(10):
        num = int(input("Digite o {}º número inteiro: ".format(i+1)))
        lista.append(num)
    
    lista_sem_negativos = remover_negativos(lista)
    
    print("Lista sem números negativos:", lista_sem_negativos)

if __name__ == "__main__":
    main()


#########################################################################################
    
# Função para calcular média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função principal
def main():
    P1 = [7.0, 8.3, 10.0, 6.5, 9.3]
    P2 = [8.5, 6.9, 5.0, 7.5, 9.8]
    
    media_P1 = calcular_media(P1)
    media_P2 = calcular_media(P2)
    
    print("Média da turma na prova 1:", media_P1)
    print("Média da turma na prova 2:", media_P2)
    
    if media_P1 > media_P2:
        print("A turma obteve a melhor média na prova 1.")
    elif media_P1 < media_P2:
        print("A turma obteve a melhor média na prova 2.")
    else:
        print("A turma obteve a mesma média nas duas provas.")

if __name__ == "__main__":
    main()


#########################################################################
    
# Função para concatenar e ordenar listas
def concatenar_ordenar(L1, L2):
    L3 = L1 + L2
    L3_crescente = sorted(L3)
    L3_decrescente = sorted(L3, reverse=True)
    return L3_crescente, L3_decrescente

# Função principal
def main():
    L1 = [4, 7, 2, 9]
    L2 = [5, 1, 8, 3]
    
    L3_crescente, L3_decrescente = concatenar_ordenar(L1, L2)
    
    print("Lista concatenada e ordenada de forma crescente:", L3_crescente)
    print("Lista concatenada e ordenada de forma decrescente:", L3_decrescente)

if __name__ == "__main__":
    main()

#########################################################################
    

# Conjuntos de filmes de cada usuário
usuario1_filmes = {"Matrix", "Inception", "The Shawshank Redemption", "Interstellar", "Pulp Fiction"}
usuario2_filmes = {"The Godfather", "Inception", "The Dark Knight", "Fight Club", "Forrest Gump"}

# União dos conjuntos
uniao = usuario1_filmes.union(usuario2_filmes)
print("União dos conjuntos de filmes:", uniao)

# Interseção dos conjuntos
intersecao = usuario1_filmes.intersection(usuario2_filmes)
print("Interseção dos conjuntos de filmes:", intersecao)

# Diferença simétrica dos conjuntos
dif_simetrica = usuario1_filmes.symmetric_difference(usuario2_filmes)
print("Diferença simétrica dos conjuntos de filmes:", dif_simetrica)



############################################################################


# Dicionário de pessoas
pessoas = {
    "12345678900": {"nome": "João", "idade": 25},
    "98765432100": {"nome": "Maria", "idade": 17},
    "56789012300": {"nome": "Pedro", "idade": 30},
    "32109876500": {"nome": "Ana", "idade": 16}
}

# Dicionário para armazenar pessoas menores de 18 anos
menores_de_18 = {}

# Removendo e movendo menores de 18 anos
for cpf, info in pessoas.items():
    if info["idade"] < 18:
        menores_de_18[cpf] = info
        del pessoas[cpf]

print("Pessoas maiores de 18 anos:", pessoas)
print("Pessoas menores de 18 anos:", menores_de_18)
