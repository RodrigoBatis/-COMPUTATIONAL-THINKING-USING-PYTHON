# Questão 01

def pares_e_impares(*args):
    dicio = {'pares' : 0, 'impares' : 0}
    for palavra in args:
        tamanho = len(palavra)
        if tamanho % 2 == 0:
            dicio['pares'] += 1
        else:
            dicio['impares'] += 1

        with open('dicio.txt', 'a') as file:
            file.write(palavra)
            file.write('\n')
    return dicio

returnFuncao01 = pares_e_impares("Abacate", "Mexirica", "Abc", "slasla")
print(returnFuncao01)

# Questão 02

dicio = pares_e_impares("Futebol", "Basquete", "Volei", "Natação", "Golfe")

import json

with open("04set2023.json", "w") as file:
    json.dump(dicio, file)

# Questão 03

def linhas_no_arquivo(nome_arquivo):
    # Forma mais comprimida
    with open(nome_arquivo, 'r+') as arquivo:
        linhas = arquivo.readlines()
        numeros_linhas = len(linhas)

        arquivo.write(str(numeros_linhas))
        arquivo.write("\n")

    # Forma mais cumprida
    # with open(nome_arquivo, 'r') as arquivo:
    #     linhas = arquivo.readlines()
    #     numeros_linhas = len(linhas)
    #
    # with open(nome_arquivo, 'a') as arquivo:
    #     arquivo.write(str(numeros_linhas))
    #     arquivo.write("\n")

linhas_no_arquivo('dicio.txt')