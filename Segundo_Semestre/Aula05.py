# lista_de_alunos = []
# lista_de_turmas = []
#
# def adiciona_aluno(nome, curso, lista_de_alunos):
#
#     dicio_aluno = {
#         "Nome": nome,
#         "Curso": curso,
#         "RM": len(lista_de_alunos)+1
#     }
#     lista_de_alunos.append(dicio_aluno)
#
# def adiciona_turma(lista_de_alunos):
#     for aluno in lista_de_alunos:
#         # {"Nome": "Fulano", "Curso": "TDS", "RM":123}
#         curso = aluno["Curso"]
#         nome = aluno["Nome"]
#         rm = aluno["RM"]
#         if rm % 2 == 0: #turma W
#             turma = "1"+curso+"W"
#         else: #turma X
#             turma = "1"+curso+"X"
#
#         dicio_turma = {
#             "Nome": nome,
#             "RM": rm,
#             "Turma": turma
#         }
#         lista_de_turmas.append(dicio_turma)
#
# #EXERCÍCICIO
# # utilizando as funções acima, crie uma lista de alunos com 5 alunos
# # e os salve em um arquivo txt , um aluno por linha
# # após isto, crie uma rotina que leia os alunos deste aquivo, passe pela função
# # adiciona turma, e salve, um aluno por linha, em um outro arquivo txt
#
# # Criar os alunos(5)
#
# adiciona_aluno("Fulano", "TDS", lista_de_alunos)
# adiciona_aluno("Ciclano", "ADM", lista_de_alunos)
# adiciona_aluno("Beltrano", "BDO", lista_de_alunos)
# adiciona_aluno("Paulo", "ESO", lista_de_alunos)
# adiciona_aluno("Fuano", "TDS", lista_de_alunos)
# print(lista_de_alunos)
#
# # Salvar a lista (um por linha)
#
# with open("lista_do_exercicio.txt", "w") as arquivo:
#     for i in lista_de_alunos:
#         arquivo.write(str(i))
#         arquivo.write("\n")
#
# # Ler este arquivo
#
# with open("lista_do_exercicio.txt", "r") as arquivo:
#     lista_lida = arquivo.readlines()
# print(lista_lida)
#
# #Converter
#
# import ast
# lista_convertida = []
# for i in lista_lida:
#     dicionario_convertido = ast.literal_eval(i)
#     lista_convertida.append(dicionario_convertido)
# print(lista_convertida)
#
# # utilizar a função "adiciona_turma"
# adiciona_turma(lista_convertida)
# print(lista_de_turmas)
#
# # salvar a lista das turmas (em um arquivo novo)
# with open("lista_de_turmas.txt","w") as arquivo:
#     for i in lista_de_turmas:
#         arquivo.write(str(i))
#         arquivo.write("\n")

# JSON = JavaScript Object Notation

import json
dicio = {
    "Nome": "Rodrigo Batista",
    "Idade": 18
}

# Para escrever o json, utilizamos o DUMP
with open("exemplo.json", "w") as arquivo:
    json.dump(dicio, arquivo)

with open("exemplo.json", "r") as arquivo:
    dicio_lido = json.load(arquivo)
print(dicio_lido.keys())

