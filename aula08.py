# Atividades sobre a aula 08
# idade1 = 30
# idade2 = 20
# idade3 = 25
################################################
# if idade3 > idade1 :
#     print("Idade 3 maior que a idade 1")
# elif idade1 > idade3 > idade2:
#     print("Idade 3 está entre as outras duas idades")
# elif idade3 == idade2 :
#     print("Idade 3 = idade 2")
# elif idade1 == idade3 :
#     print("Idade 1 = idade 3")
# elif idade3 == idade1 == idade2:
#     print("Todas as 3 idades são iguais")
# else:
#     print("Idade 3 é menor que as outras duas idades")
################################################
# if 1 > 0 :
#     print("1")
# elif 2 > 0  :
#     print("2")
# elif 3 > 0 :
#     print("3")
# else:
#     print("4")
#################################################
# if 1 > 0:
#     print("1")
# if 2 > 0:
#     print("2")
# if 3 > 0 :
#     print("3")
# else:
#     print("4")
#################################################
# if idade1 > idade2:
#     dif = idade1 - idade2
#     print("A diferença entre as idades é de {}".format(dif))
# elif idade2 > idade:
#     dif = idade2 - idade1
#     print("A diferença entre de idades é de {}".format(dif))
# else:
#     print("As idades são iguais")
#################################################

nomeUsuario1 = input("Digite o primeiro nome: ")
nomeUsuario2 = input("Digite o segundo nome: ")
qtddLetrasUsuario1 = len(nomeUsuario1)
qtddLetrasUsuario2 = len(nomeUsuario2)

if qtddLetrasUsuario1 > qtddLetrasUsuario2 :
    dif = int(qtddLetrasUsuario1 - qtddLetrasUsuario2)
    vezes = int(qtddLetrasUsuario1 / qtddLetrasUsuario2)
    print("O nome {} é {} caracteres maior que o nome {}".format(nomeUsuario1, dif, nomeUsuario2))
    print("O nome {} é {} vezes maior que o nome {}".format(nomeUsuario1, vezes, nomeUsuario2))
elif qtddLetrasUsuario2 > qtddLetrasUsuario1 :
    dif = int(qtddLetrasUsuario2 - qtddLetrasUsuario1)
    vezes = int(qtddLetrasUsuario2 / qtddLetrasUsuario1)
    print("O nome {} é {} caracteres maior que o nome {}".format(nomeUsuario2, dif, nomeUsuario1))
    print("O nome {} é {} vezes maior que o nome {}".format(nomeUsuario2, vezes, nomeUsuario1))

else:
    print("A quantidade de caracteres de ambos dos nomes são iguais")

#################################################################




