#EXERCÍCIO:
# como vocês manipulariam uma string contendo um dicionário para formar um dicionário?
# ex: "{'Nome': 'Fulano', 'Curso': 'TDS', 'RM': 1}"

ex = "{'Nome': 'Fulano', 'Curso': 'TDS', 'RM': 1}"
#
# quebra = ex.split(",")
# for i in quebra:
#     if i == quebra[0]: #isolei a abertura da chave
#         #Opcão 1
#         # print(i.split("{")[-1])
#         #Opção 2
#         print(i[1:].split(":"))
#         chave = i[1:].split(":")[0]
#         valor = i[1:].split(":")[1]
#         # dicionario_linha[chave] = valor
#     elif i == quebra[-1]: #isolei o fechamento da chave
#         #Opcão 1
#         print(i.split("}")[0].split(":"))
#         #Opção 2
#         # print(i[:-1])
#     else:print(i.split(":"))


with open("lista_de_alunos.txt", "w+") as arquivo:
    arquivo.write("Teste")
    # print()
