### EXERCÍCIOS:

## 1) refaçam o exercício anterior, mas agora com while

# i=0
# print("Tabuada do 5")
# while i<=10:
#     print(f"{5} X {i} = {i*5}")
#     i+=1

## 2) Solicite dois número ao usuário, sendo que o segundo deverá ser obrigatoriamente maior que o primeiro

# num1 = float(input("Digite o primeiro numero: "))
# num2 = float(input("Digite o segundo numero sendo maior que o primeiro: "))
#
# while num2 <= num1 :
#     print("O segundo número não é maior que o primeiro")
#     num2 = float(input(f"Diga um número maior que {num1}: "))


## 3) Solicitar um número obrigatoriamente inteiro positivo do usuário, e calcular seu fatorial

# n = float(input("Digite um numero inteiro positivo: "))
#
# # while float(n)//1!=n or n < 0:
# #     n = float(input("Digite um numero inteiro positivo: "))
#
# while int(n)!=n or n < 0:
#     n = float(input("Digite um numero inteiro positivo: "))
#
# fatorial = 1
# n=int(n)
#
# for i in range(1,n+1):
#     fatorial*=i
# print("O fatorial de {} é {}".format(n, fatorial))
#
# fatorial = 1
#
# for i in range(n,0,-1):
#     fatorial*=i
# print("O fatorial de {} é {}".format(n, fatorial))

## 4) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive

fatorial =1

for i in range(1, 100+1):
    fatorial += i
print("A soma total é {}".format(fatorial))