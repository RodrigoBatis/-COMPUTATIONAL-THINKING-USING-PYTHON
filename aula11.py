'''
## EXERCÍCIO:
# Faça um programa em loop que imprima esta imagem:
*
**
***
****
*****
****
***
**
*
'''

# estrela = "*"
# for i in range(1,10):
#     if i<=5:
#         print(estrela*i)
#     else:
#         print(estrela*(10-i))

# n= int(input("Diga a quantidade de linhas (ímpar): "))
# estrela = "*"
# for i in range(1,n+1):
#     if i<= (n//2+1):
#         print(estrela*i)
#     else:
#         print(estrela*((n+1)-i))

## WHILE (enquanto)

#Imprimindo de 0 a 4

# numero = 0
# while numero <=4:
#     print(numero)
#     numero+=1

# #Corigindo todos os possiveis erros do for com while
# num = int(input("Diga a quantidade de linhas (ímpar): "))
#
# while num%2==0 or num < 0:
#     if num%2==0 and num < 0:
#         print("O numero digitado é par e negativo digite outro numero: ")
#         num = int(input("Diga a quantidade de linhas (ímpar): "))
#     elif num%2==0 :
#         print("O numero digitado é par digite outro numero: ")
#         num = int(input("Diga a quantidade de linhas (ímpar): "))
#     else :
#         print("Esse numero é negativo digite um numero impar")
#         num = int(input("Diga a quantidade de linhas (ímpar): "))
#
# estrela = "*"
# for i in range(1,num+1):
#     if i<= (num//2+1):
#         print(estrela*i)
#     else:
#         print(estrela*((num+1)-i))


#### Praticando

#Imprima a tabuada do numero 5, entre 0 e 10 for

# print("----- Tabuada do 5 FOR -----")
# num = 5
# for i in range(11):
#     print(f"{num} X {i} = {num*i}")

#Imprima a tabuada do numero 5, entre 0 e 10 while
num = 5
contador = 0
print("----- Tabuada do 5 WHILE -----")
while contador <= 10:
    print(f"{num} X {contador} = {num*contador}")
    contador+=1


