import math

Idade_Alvo = 65
Minha_idade = 18

# print("Normal: ", Idade_Alvo)
# print("Formatando {}".format(Idade_Alvo))
# print("Segunda forma {Idade_Alvo}")
# print("Terceira forma {i}, outro exemplo {n}"\
#       .format(i=Idade_Alvo, n=Minha_idade))
#
# string_original = "30"
# convertido_em_int = int(string_original)
# convertido_em_float = float(string_original)
#
# idade_convertida_em_string = str(Minha_idade)
# print(type(idade_convertida_em_string))

ex_float_1 =30.0
ex_float_2 =30.1
ex_float_3 =30.9

# print(int(ex_float_1))
# print(int(ex_float_2))
# print(int(ex_float_3))

#operadores aritméticos
# O resultado de uma divisão em python vai ser sempre float
# + - * /
# % // **

# #divisão normal
# print("divisão normal", 13/5)
# #modulo -- mostra a quantidade maxima de vezes que se repete sem ultrapassar o limite
# print("modulo", 12//5)
# #resto
# print("resto", 13%5)
# #expoente
# print(5**2)
# #raiz quadrada (square root) -> sqrt
# ##nome_da_biblioteca.funcao
# ###retorna um float
# print("raiz quadrada", math.sqrt(144))

# comparadores
# = é definição
# == é comparação
# > < == !=
# >= <=

# print(5<2)
# print(type(5<2))
# print(5==5)
# print(5>=2)
# print(5 != 2)
# print(type(5)==type(5.0))

#Exercicios

Nome_pessoa1    = input("Digite o primeiro nome:")
print()
Idade_pessoa1   = input("Digite a primeira idade:")
print()
Nome_pessoa2    = input("Digite o segundo  nome:")
print()
Idade_pessoa2   = input("Digite a segunda idade:")
print()

Idade_pessoa1_inteiro = int(Idade_pessoa1)
Idade_pessoa2_inteiro = int(Idade_pessoa2)

soma_idades = Idade_pessoa1_inteiro + Idade_pessoa2_inteiro
media = soma_idades/2
diferenca = Idade_pessoa1_inteiro - Idade_pessoa2_inteiro

print("{s} é mais velho(a) que o(a) {n}?".format(s =Nome_pessoa1, n = Nome_pessoa2)\
      , Idade_pessoa1_inteiro > Idade_pessoa2_inteiro)
print("A diferença entre {s} e {n} é de {m} anos!".format(s=Nome_pessoa1, n=Nome_pessoa2, m=diferenca))
print("A média das idades é de {} anos!".format(media))
