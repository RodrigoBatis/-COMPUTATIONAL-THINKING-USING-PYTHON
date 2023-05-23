# i=0

# print("while com break")
# while i<=5:
#     if i==3:break
#     print(i)
#     i+=1

# print("while com pass")
# while i<=5:
#     if i==3:pass
#     print(i)
#     i+=1

# print("while com continue")
# while i<=5:
#     if i==3:continue
#     print(i)
#     i+=1

### EXERCÍCIOS

# 1) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# # Feito com For
# soma = 0
# for i in range(1, 101):
#     soma += i
# print("A soma total é {} ".format(soma))
#
# # Feito com While
# contador = 0
# soma_while = 0
# while contador <= 100:
#     soma_while += contador
#     contador+=1
# print("A soma total é {} ".format(soma_while))

##Caso quissese todos:
###For

# soma=0
# for i in range(1,101):
#     soma+=i
#     print(f"A soma dos números inteiros positivos de 1 a {i} é {soma}")

###While
# contador = 0
# while contador <= 100:
#     soma_

# 2) imprima a tabuada do número 5, de 0 e 10, inclusive.
# Depois, adapte o programa para receber dois números do usuário: o de início e o de fim
# faça este exercício uma vez utilizando o for, e outra utilizando o while

##For

n1 = float(input("Digite um número inteiro para o início da tabuada: "))

while int(n1)!=n1:
    print("Número digita inválido!")
    n1 = float(input("Digite um número inteiro para o início da tabuada: "))

n2 = float(input("Digite um número inteiro para o final da tabuada: "))

while int(n2)!=n2:
    print("Número digita inválido!")
    n2 = float(input("Digite um número inteiro para o final da tabuada: "))

n1=int(n1)
n2=int(n2)
# for i in range(n1,n2+1,1):
#     print(f"{n1} X {i} = {n1*i}")

# i=0
# print("Tabuada do 5")
# while i<=10:
#     print(f"{5} X {i} = {i*5}")
#     i+=1

# 3) solicite 2 números ao usuário. Para cada número do 1 ao primeiro número, faça a tabuada dele do 0 até o segundo número

# for i in range(1,n1+1):
#     print(f"--- Tabuada do ", i)
#     for j in range(n2+1):
#         print(f"{i} X {j} = {i*j}")
#     print()

i=1
while i > 0 and i <=n1:
    print(f"--- Tabuada do ", i)
    j=0
    while j <= n2:
        print(f"{i} X {j} = {i * j}")
        j+=1
    i+=1
    print()