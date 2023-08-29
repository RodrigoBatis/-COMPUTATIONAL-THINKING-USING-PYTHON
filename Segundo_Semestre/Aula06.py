'''
BUSCA em listas ordenas

Para encontrar um item em uma lista ordenada, podemos utilizar a
busca Binária, que consiste em sempre comparar se o item a ser encontrado
é maior que o valor correspondente ao indice do meio da lista,
oque gera uma resposta binária:
True ou False

Com isto, independente do tamanho da lista, temos uma quantidade máxima
fixade tentativas até encontrar o item ou chegar à conclusão que
ele não existe

Ex: encontrar um minuto exato 26 num rélogio (0-59)
    - 1.1: comparamos com valor do índice do meio: 29 -> False
    - 1.2: pegar a metade correspondente da lista: 0-29
    - 2.1: comparando com o valor do índice do meio: 14 -> True
    - 2.2: pegar a metade correspondente da lista: 15-29
    - 3.1: comparamos com o valor do índice do meio: 21 -> True
    - 3.2: pegar a metade correspondente da lista: 21-29
    - 4.1: comparamos com o valor do indice do meio: 25 -> True
    - 4.2: pegar a metade correspondente da lista: 25-29
    - 5.1: comparamos com o valor do indice do meio: 27 -> False
    - 5.2: pegar a metade correspondente da lista: 25-27
    - 6.1: comparamos com o valor do indice do meio: 26 -> False
    - 6.2: pegar a metade correspondente da lista: 25-26
    - 7.1: comparamos com o valor do indice do meio: 25 -> True
    - 7.2: pegar a metade correspondente da lista: 26 <- ENTRAR COM CRITÉRIO DE PARADA
'''

# Vamos colocar isto em python
# (Implementar um busca binária em uma lista ORDENADA)

# relogio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
#      32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]

lista = [i for i in range(11)]
target = 5

for i in range(len(lista)):
    indice_meio = lista[len(lista)//2]
    valor_meio = lista[indice_meio]
    if target > valor_meio:
        lista = lista[indice_meio:]
    elif target == valor_meio:
        print("Encontrado no indice", indice_meio)
        break
    else:
        lista = lista[:indice_meio]
    print(lista)
    break


