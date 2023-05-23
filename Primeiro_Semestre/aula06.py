#exercício da aula anterior
## calcular o menor número de notas necessárias para pagar
# este custo mensal

#ainda falta descobrir o quanto o troco importa
# completar o problema utilizando moedas para chegar ao valor exato

custo_mensal = 266.66
quanto_falta = custo_mensal%200
#[...]

#substitui o valor do "quanto_falta"
# quanto_falta = quanto_falta%10
# quanto_falta = quanto_falta-10
# quanto_falta-= 10
#print(266.66%200) # =266.66 - (266.66//200 * 200)

# ESTRUTURAS CONDICIONAIS - simples (if) - "se"

# if 1>0:
#     #dentro do if
#     print("1>0")
#     print("blablabla")
#     print("outra linha")
#     contador = 1
#     if 2==0:
#         print(contador)
#         contador+=1
#         print(contador)
#     contador+=1
#     #numero1=input("qualquer coisa")
#     print(contador)
# #estou fora do if

# minha_idade=30
# idade_colega=40
#if aceita composições
# if minha_idade>idade_colega:
#     print("você é mais velho ")
#
# # else = Todo o resto
# else:  #você não escreve condições
#     print("você não é mais velho")

#utilizando apenas if e else, faça um programa que diga
# a diferença de idade entre você e um colega, e seus nomes,
# sem que a resposta seja um número negativo

# seu_nome = input("Diga seu nome: ")
# sua_idade = float(input("Olá,{}\nDiga a sua idade ".format(seu_nome)))
#
#
# nome_do_colega = input("Diga o nome do seu colega: ")
# idade_colega = float(input("Olá {}, amigo de {}\nDiga a idade de um colega ".\
#                      format(nome_do_colega,seu_nome)))
# ## primeira forma de fazer
# diferenca_de_idade=sua_idade-idade_colega
#
# if diferenca_de_idade<0:
#     diferenca_de_idade *= (-1)
#     print(diferenca_de_idade)
# else:
#     print(diferenca_de_idade)
#
# ## segunda forma de fazer
# if sua_idade>idade_colega:
#     print(sua_idade-idade_colega)
# else:
#     print(idade_colega-sua_idade)
#
# ## terceira forma
# if sua_idade-idade_colega>0:
#     print(sua_idade-idade_colega)
# else:
#     print(idade_colega - sua_idade)
#     #ou
#     print((sua_idade-idade_colega)*(-1))
#

#cada else "fecha" um if

# variavel = 2
#
# if variavel==2:
#     variavel+=1
#     print(variavel)
#
# print(variavel)
#
# if variavel==2:
#     variavel+=2
#
# print(variavel)


#Exercício:
#utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e seus respectivos nomes, e diga:
## a diferença de idade entre vocês, chamando pelo nome, sem que a resposta seja um número negativo
## quantas vezes a pessoa mais velha é mais velha que a mais nova, limitando a resposta a 2 casas decimais
## para cada pessoa, diga:
### se ela for maior de idade, há quanto tempo ela fez 18 anos E quanto tempo falta para se aposentar (assumindo que a idade de aposentadoria é 75 anos);
### se ela for menor de idade, quantos anos faltam para ela fazer 18 anos E se ela ainda é criança (menor de 12 anos) ou já é adolescente (maior ou igual a 12 anos)


## 1- a diferença de idade entre vocês, chamando pelo nome, sem que a resposta seja um número negativo
### Minha opção maluca

# primeiro_nome = input(" Digite seu nome: ")
# segundo_nome  = input(" Digite o nome do seu amigo: ")
#
# primeira_idade = int(input(" {} qual sua idade? ".format(primeiro_nome)))
# segunda_idade  = int(input(" {} qual seu idade? ".format(segundo_nome)))
#
# mais_velho = primeira_idade > segunda_idade;
#
# if mais_velho == True:
#     diferenca_idade = primeira_idade - segunda_idade
#     print(" A diferença de idade entre {} e {} é de {}, sendo {} mais velho ".format(primeiro_nome, segundo_nome, diferenca_idade, primeiro_nome))
#
# else:
#     diferenca_idade = segunda_idade - primeira_idade
#     print(" A diferença de idade entre {} e {} é de {}, sendo {} mais velho ".format(primeiro_nome, segundo_nome, diferenca_idade, segundo_nome))

## 2- quantas vezes a pessoa mais velha é mais velha que a mais nova, limitando a resposta a 2 casas decimais

primeiro_nome = input(" Digite seu nome: ")
segundo_nome  = input(" Digite o nome do seu amigo: ")

primeira_idade = int(input(" {} qual sua idade? ".format(primeiro_nome)))
segunda_idade  = int(input(" {} qual seu idade? ".format(segundo_nome)))

mais_velho = primeira_idade > segunda_idade;

if mais_velho == True:
    diferenca_idade = primeira_idade - segunda_idade
    vezes_mais_velho = primeira_idade / segunda_idade
    print(" A diferença de idade entre {} e {} é de {}, sendo {} mais velho ".format(primeiro_nome, segundo_nome, diferenca_idade, primeiro_nome))
    print(" {} é {:.2f} vezes mais velho que {} ".format(primeiro_nome, vezes_mais_velho, segundo_nome))

else:
    diferenca_idade = segunda_idade - primeira_idade
    vezes_mais_velho = segunda_idade / primeira_idade
    print(" A diferença de idade entre {} e {} é de {}, sendo {} mais velho ".format(primeiro_nome, segundo_nome, diferenca_idade, segundo_nome))
    print(" {} é {:.2f} vezes mais velho que {} ".format(segundo_nome, vezes_mais_velho, primeiro_nome))

### 3- se ela for maior de idade, há quanto tempo ela fez 18 anos E quanto tempo falta para se aposentar
# (assumindo que a idade de aposentadoria é 75 anos);
### se ela for menor de idade, quantos anos faltam para ela fazer 18 anos E se ela ainda é criança
# (menor de 12 anos) ou já é adolescente (maior ou igual a 12 anos)

#Tratando a idade da primeira pessoa
if primeira_idade >= 18:
    quanto_tempo_fez_18 = primeira_idade - 18
    tempo_aposentadoria = 75 - primeira_idade
    print(" {} você já é de maior há {} anos! ".format(primeiro_nome, quanto_tempo_fez_18))
    print(" {} faltam exatos {} anos para sua aposentadoria ".format(primeiro_nome, tempo_aposentadoria))
else :
    tempo_para_fazer_18 = 18 -primeira_idade
    print(" {} faltam exatos {} anos para maioridade ".format(primeiro_nome, tempo_para_fazer_18))
    if primeira_idade >= 12:
        print(" {} você já é um adolecente ".format(primeiro_nome))
    else :
        print(" {} você ainda é uma criança ".format(primeiro_nome))

#Tratando a idade sa segunda pessoa
if segunda_idade >= 18:
    quanto_tempo_fez_18 = segunda_idade - 18
    tempo_aposentadoria = 75 - segunda_idade
    print(" {} você já é de maior há {} anos! ".format(segundo_nome, quanto_tempo_fez_18))
    print(" {} faltam exatos {} anos para sua aposentadoria ".format(segundo_nome, tempo_aposentadoria))
else :
    tempo_para_fazer_18 = 18 -segunda_idade
    print(" {} faltam exatos {} anos para maioridade ".format(segundo_nome, tempo_para_fazer_18))
    if primeira_idade >= 12:
        print(" {} você já é um adolecente ".format(segundo_nome))
    else :
        print(" {} você ainda é uma criança ".format(segundo_nome))



