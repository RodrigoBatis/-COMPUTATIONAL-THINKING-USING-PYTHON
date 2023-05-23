#Exercicio 1

# n1= float(input("Diga um número inteiro: "))
# while n1//1!=n1:
#     print("Você não digitou um numero inteiro")
#     n1 = float(input("Diga um número inteiro: "))
# n2= float(input("Diga outro número inteiro, maior que o primeiro: "))
# while n2//1!=n2 or n2<=n1:
#     print("Você não digitou um número inteiro ou digitou um número maior ou igual ao primeiro")
#     n2 = float(input(f"Diga outro número inteiro, maior que o {n1}: "))
# n1=int(n1)
# n2=int(n2)
# soma=0
# for i in  range(n1+1, n2+1):
#     soma+=i
#
# print(f"A soma é {soma}")

#Exercicio 2

# n1=float(input("Diga um numero inteiro negativo: "))
# while n1//1!=n1 or n1>=0:
#     print("Você não digitou um número inteiro negativo")
#     n1 = float(input("Diga um numero inteiro negativo: "))
#
# n2=float(input("Diga um numero inteiro negativo diferente do primeiro: "))
# while n2//1!=n2 or n2>=0 or n2==n1:
#     print("Você não digitou um número inteiro negativo")
#     n2=float(input("Diga um numero inteiro negativo diferente do primeiro: "))
#
# n1=int(n1)
# n2=int(n2)
#
# if n1>n2:
#     for i in range(n1-1, n1-7,-1):
#         print(i)
#     print()
#     for i in range(n2+1, n2+6):
#         print(i)
# else:
#     for i in range(n2-1, n2-7,-1):
#         print(i)
#     print()
#     for i in range(n1+1, n1+6):
#         print(i)

#Exercicio 3

n1=float(input("Diga um número ímpar positivo: "))

while n1%2==0 or n1<0:
    if n1%2==0 and n1<0:
        print("Você digitou um número par e negativo")
        n1 = float(input("Diga um número ímpar positivo: "))
    elif n1%2==0:
        print("Você digitou um número par")
        n1 = float(input("Diga um número ímpar positivo: "))
    else:
        print("Você digitou um número negativo")
        n1 = float(input("Diga um número ímpar positivo: "))

n2=float(input("Diga um número par negativo: "))

while n2%2!=0 or n2>0:
    if n2%2!=0 and n2>0:
        print("Você digitou um numero impar positivo")
        n2 = float(input("Diga um número par negativo: "))
    elif n2%2!=0:
        print("Você digitou um número impar")
        n2 = float(input("Diga um número par negativo: "))
    else:
        print("Você digitou um número positivo")
        n2 = float(input("Diga um número par negativo: "))

if n1//1!=n1 or n2//1!=n2:
    parte_decimal_n1 = n1 - (n1//1)
    parte_decimal_n2 = n2 - (n2//1)
    if parte_decimal_n1>parte_decimal_n2:
        print(f"N1 ({n1}) possui a maior parte decimal")
    elif parte_decimal_n2>parte_decimal_n1:
        print(f"N2 ({n2}) possui a maior parte decimal")
    else:
        print(f"A partes decimais do N1({n1}) e N2({n2}) são iguais")
else:
    print("Os dois números são inteiros")

