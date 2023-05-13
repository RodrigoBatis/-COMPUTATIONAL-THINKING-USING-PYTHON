### EXERCÍCIOS ADICIONAIS

#1) escreva uma função que receba como argumento um número e retorne seu fatorial

def fatorial(n):
    fatorial = 1
    while n>0:
        fatorial*=n
        n-=1
    return fatorial

# print(f"O fatorial do número digitado é {fatorial(10)}")

#2) escreva uma função que solicite ao usuário um número e force para que ele seja positivo e inteiro,
# e retorne este número

def numero_positivo_inteiro ():
    n = float(input("Digite um numero inteiro positivo: "))
    while n!=int(n) or n<0:
        print("Você não digitou um número inteiro e positivo")
        n = float(input("Digite um numero inteiro positivo: "))
    return n

# print(f"O numero ditado anteriormente é {numero_positivo_inteiro()}")

#3) escreva uma função que chame combine as funções dos exercícios anteriores
# (ou seja, uma função sem parâmetros que utilize o retorno da segunda função como parâmetro da primeira)

def combinacao():
    n = numero_positivo_inteiro()
    resposta =fatorial(n)
    return resposta

# print(combinacao())

#4) Crie uma função que receba uma palavra e retorne ela toda em letras maiúsculas

def maiusculas (palavra):
    return palavra.upper()

# print(maiusculas("rodrigo batista freire"))

#5) Cria uma função que receba uma palavra e uma condição ('maiúscula' ou 'minúscula') e retorne a palavra na
# condição solicitada

def maiuscula_minuscula (palavra, condicao):
    if condicao == "maiuscula":
        return palavra.upper()
    elif condicao == "minuscula":
        return palavra.lower()
    else:return "Condiçao invalida"

# print(maiuscula_minuscula("ROdrigo", "maiuscula"))

#6) Crie uma função que receba 2 números (inicio e fim), e imprima os números pares neste intervalo
# (incluindo o início e fim)

def intervalo_pares_entre_numeros(inicio, fim):
    for i in range(inicio, fim):
        if i%2==0:
            print(i)

# intervalo_pares_entre_numeros(0,10)

#7) Crie uma função que receba 2 números e imprima sua soma, multiplicação, divisão e subtração.
# Estes prints deverão ser formatados para serem bem explícitos no que está sendo mostrado (incluindo os
# números originais);
# E esta função deverá estar devidamente documentada, explicando tudo o que ela realiza, seus parâmetros e
# possíveis retornos

def operacoes (n1,n2):
    """
    função responsavel por realisar e imprimir as quatro operações basicas matematicas elas são:
    (Soma, Multiplicação, Divisão e Subtração)
    :param n1: Podendo ser um float ou int
    :param n2: Podendo ser um float ou int
    :return: Apenas a impressão do resultado das operações
    """
    soma = n1+n2
    multiplicacao = n1*n2
    divisao = n1/n2
    subtracao = n1-n2

    print(f"O resultado da soma de {n1} com {n2} é {soma}")
    print(f"O resultado da multiplicação de de {n1} com {n2} é {multiplicacao}")
    print(f"O resultado da divisão de {n1} por {n2} é {divisao}")
    print(f"O resultado da subtração de {n1} com {n2} é {subtracao}")

# operacoes(5, 10)