'''
1)
Crie uma função que receba uma string como parâmetro
esta função deverá criar e reotrnar um dicionário novo onde as chaves
deste dicionário são as diferentes letras desta string; e os valores,
suas quantidades
'''

def funcao01(string):
    dicio={}

    for i in string:
        if i not in dicio.keys():
            dicio[i] = 1
        else:
            dicio[i] += 1
    return dicio

novo_dicio = funcao01("teste")
print(novo_dicio)
print()

'''
2) utilize a função acima para criar pelo menos 3 dicionários, e
adicioná-los a uma lista
'''
lista=[]
lista.append(funcao01("exemplo"))
lista.append(funcao01("palavra"))
lista.append(funcao01("teclado"))

print(lista)
print()

'''
3) crie uma função que receba uma lista de dicionários como parâmetro,
e salve cada dicionário em um arquivo json único, cujo nome deverá ser
um contador criado por você que garanta que ele é único por lista
'''
def salva_lista(lista):
    import json
    id = 0
    nome_base = "dicio"

    for dicio in lista:
        nome_arquivo = nome_base + str(id) + ".json"

        with open(nome_arquivo, "w") as arquivo:
            json.dump(dicio, arquivo)

        id += 1

salva_lista(lista)
print()