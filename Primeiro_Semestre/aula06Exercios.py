#EXERCÍCIO

'''
utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e
seus respectivos nomes, e diga, colocando os nomes nas respostas:
1) se seus nomes possuem a mesma quantidade de letras
2) quantos porcento a idade do mais velho representa da idade do mais novo,
limitando a resposta a 1 casa decimal E 
a) se a pessoa mais velha é maior de idade
b) se a pessoa mais nova é uma criança (possui menos de 12 anos)
3) para cada pessoa, diga:
a) se ela for maior de idade, se ela já se aposentou OU quanto tempo falta para se aposentar
(assumindo que a idade de aposentadoria é 75 anos);
b) se ela for menor de idade, qual sua idade em meses

OBS: criem casos de teste para todas as possibilidades que vocês identificarem
'''

primeiroNome = input("Digite o primeiro nome: ")
segundoNome = input("Digite o segundo nome: ")
primeiraIdade = int(input("{} digite sua idade: ".format(primeiroNome)))
segundaIdade = int(input("{} digite sua idade: ".format(segundoNome)))
quantidadeLetras = len(primeiroNome) == len(segundoNome)

#Exercicio 1


if quantidadeLetras == 1 :
    print("{} e {} possuem a mesma quantidade letras no nome! ".format(primeiroNome, segundoNome))
    print()
else:
    print("{} e {} não possuem a mesma quantidade de letras no nome! ".format(primeiroNome, segundoNome))
    print()

#Exercicio 2

if segundaIdade > primeiraIdade :
    porcetagemIdade = (primeiraIdade/segundaIdade)
    print("{} é {:.1%} mais velho que o {}".format(primeiroNome, porcetagemIdade, segundoNome))
else:
    porcetagemIdade = (segundaIdade / primeiraIdade)
    print("{} é {:.1%} mais velho que o {}".format(segundoNome, porcetagemIdade, primeiroNome))

#Exercicio 2 A e B

if primeiraIdade > segundaIdade:
    if primeiraIdade >= 18 :
        print("{} é maior de idade!".format(primeiroNome))
    else:
        print("{} é menor de idade!".format(primeiroNome))

    if segundaIdade < 12 :
        print("{} é uma criança!".format(segundoNome))
    else:
        print("{} não é uma criança!".format(segundoNome))
else:
    if segundaIdade >= 18 :
        print("{} é maior de idade".format(segundoNome))
    else:
        print("{} é menor de idade!".format(segundoNome))

    if primeiraIdade < 12 :
        print("{} é uma criança!".format(primeiroNome))
    else:
        print("{} não é uma criança!".format(primeiroNome))

#Exercio 3

if primeiraIdade >= 18:
    print("Faltam exatos {} anos para {} se aposentar!".format(75 - primeiraIdade, primeiroNome))
else:
    print("{} você possui {} meses de vida!".format(primeiroNome, primeiraIdade * 12))

if segundaIdade >= 18:
    print("Faltam exatos {} anos para {} se aposentar!".format(75 - segundaIdade, segundoNome))
else:
    print("{} você possui {} meses de vida!".format(segundoNome, segundaIdade * 12))



