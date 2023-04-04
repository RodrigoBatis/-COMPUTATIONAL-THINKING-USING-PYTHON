'''
Exercícios:

1)Solicite um número do usuário. Diga a menor nota de real que é maior que este número. 
Caso não exista, diga “Este número é muito grande para ser pago com apenas 1 nota de real”
'''

numero=float(input("Favor digitar um número: "))

#Crescente
if 0 > numero:
    print("Esse numero é negativo")
elif 2 > numero :
    print("A menor nota maior que {} é a de 2 reais ".format(numero))
elif 5 > numero >= 2 :
    print("A menor nota maior que {} é a de 5 reais ".format(numero))
elif 10 > numero >= 5 :
    print("A menor nota maior que {} é a de 10 reais ".format(numero))
elif 20 > numero >= 10 :
    print("A menor nota maior que {} é a de 20 reais ".format(numero))
elif 50 > numero >= 20 :
    print("A menor nota maior que {} é a de 50 reais ".format(numero))
elif 100 > numero >= 50 :
    print("A menor nota maior que {} é a de 100 reais ".format(numero))
elif 200 > numero >= 100 :
    print("A menor nota maior que {} é a de 200 reais ".format(numero))
elif 200 <= numero :
    print("Não existe nota em real maior do que {} ".format(numero))
else:
    print("else - situação não prevista")

#Decrecente
if numero < 0:
    print("Esse numero é negativo")
elif numero >= 200 :
    print("Não existe nota em real maior do que {} ".format(numero))
elif numero < 200 and numero >= 100 :
    print("A nota maior que {} é 200 reais".format(numero))
elif numero < 100 and numero >= 50 :
    print("A nota maior que {} é 100 reais".format(numero))
elif numero < 50 and numero >= 20 :
    print("A nota maior que {} é 50 reais".format(numero))
elif numero < 20 and numero >= 5 :
    print("A nota maior que {} é 20 reais".format(numero))
elif numero < 5 and numero >= 2 :
    print("A nota maior que {} é 5 reais".format(numero))
elif numero < 2 and numero >= 0 :
    print("A nota maior que {} é 2 reais".format(numero))
else:
    print("else - situação não prevista")

'''
2)Solicite um número ao usuário. Diga se este número é igual a 0. Se não for, diga se ele é par ou ímpar
'''
if numero == 0 :
    print("O número digitado ({}) é igual a 0".format(numero))
elif numero % 2 == 0 :
    print("O numero digitado {} é par sendo diferente de 0".format(numero))
else:
    print("O numero digitado {} é impar sendo diferente de 0".format(numero))

'''
3)Solicite 3 números ao usuário. Diga o menor deles
'''
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero2 > numero < numero3 :
    print("Numero 1 ({}) é o menor".format(numero))
elif numero > numero2 < numero3 :
    print("Numero 2 ({}) é o menor".format(numero2))
elif numero > numero3 < numero2 :
    print("Numero 3 ({}) é o menor".format(numero3))
elif numero == numero2 == numero3 :
    print("Todos são iguais, então podemos dizer que {} é o menor".format(numero))
elif numero == numero2:
    if numero > numero3:
        print("Numero 3 ({}) é o menor".format(numero3))
    else:
        print("Os menores numeros são iguais ({}), e são o numero 1 e 2".format(numero))
elif numero == numero3:
    if numero > numero2:
        print("Numero 2 ({}) é o menor".format(numero2))
    else:
        print("Os menores numeros são iguais ({}), e são o numero 1 e 3".format(numero))
elif numero2 == numero3:
    if numero2 > numero:
        print("Numero 1 ({}) é o menor".format(numero))
    else:
        print("Os menores numeros são iguais ({}), e são o numero 2 e 3".format(numero2))
else:
    print("Situação inesperada inicialmente")

'''
4)Solicite ao usuário (separadamente) o mês do ano, e o dia atual. Diga em qual estação estamos
    Outono      : De 22 de março    a 21 de junho.
    Inverno     : De 22 de junho    a 23 de setembro.
    Primavera   : De 24 de setembro a 21 de dezembro.
    Verão       : De 22 de dezembro a 21 de março.
'''
mes = input("Digite o mês do ano que está: " )
dia = int(input("Digite o dia do mês que está: "))


## MATCH/CASE
#Ele foi pensado para igualdades

num = 3

match num:
    case 0:
        print("O numero é 0")
    case 1:
        print("O numero é 1")
    case 2:
        print("O numero é 2")
    case _:
        print("{} é um número que não é 0,1 ou 2")

#Exemplo de comparação de desigualdade no match/case

num = 3

match num:
    case _ if num > 0:
        print("O numero é maior que 0")
    case _ if num < 0:
        print("O numero é menor que 0")

############################################################