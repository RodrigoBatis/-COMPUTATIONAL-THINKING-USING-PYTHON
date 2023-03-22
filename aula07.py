#Calculando a diferença de caracteres entre os dois
nomeUsuario = input("Digite seu nome: ")
nomeColega = input("Digite o nome do seu colega: ")

quantidadeLetrasUsuario = len(nomeUsuario)
quantidadeLetrasColega  = len(nomeColega)

if quantidadeLetrasUsuario > quantidadeLetrasColega :
    vezes = quantidadeLetrasUsuario/quantidadeLetrasColega
    print("{} possui {} letras, e isto é {:.2f} vezes"
          " maior do que o {} que possui {} letras".format(nomeUsuario, quantidadeLetrasUsuario,
                                                           vezes, nomeColega, quantidadeLetrasColega))
else:
    vezes = quantidadeLetrasColega / quantidadeLetrasUsuario
    print("{} possui {} letras, e isto é {:.2f} vezes"
          " maior do que o {} que possui {} letras".format(nomeColega, quantidadeLetrasColega,
                                                           vezes, nomeUsuario, quantidadeLetrasUsuario))
#Pedindo a altura dos dois

alturaUsuario = float(input("{} digite a sua altura em cm:".format(nomeUsuario)))
alturaColega  = float(input("{} digite a sua altura em cm:".format(nomeColega)))
mediaAlturaNBA = 201

#4 - Usuario
if alturaUsuario>=mediaAlturaNBA:
    diferencaAltura = mediaAlturaNBA - alturaUsuario
    print("{} é {} mais alto que a média da NBA".format(nomeUsuario, diferencaAltura))
else:
    resposta = ((mediaAlturaNBA - alturaUsuario)/alturaUsuario)* 100
    print("{} você precisaria de {:.3f}% a mais da sua propria altura para chegar à média".format(nomeUsuario, resposta))

# - Colega
if alturaColega >= mediaAlturaNBA:
    diferencaAltura = mediaAlturaNBA - alturaColega
    print("{} é {} mais alto que a média da NBA".format(nomeColega, diferencaAltura))
else:
    resposta = ((mediaAlturaNBA - alturaColega)/alturaColega)* 100
    print("{} você precisaria de {:.3f}% a mais da sua propria altura para chegar à média".format(nomeColega, resposta))

#Solicitando a idade dos usuarios
# 5

idadeUsuario = int(input("{} digite sua idade: ".format(nomeUsuario)))
idadeColega = int(input("{} digite sua idade: ".format(nomeColega)))

#6
if idadeUsuario == idadeColega:
    print("As idades de {} e {} são iguais".format(idadeUsuario, idadeColega))
else :
    if idadeUsuario < idadeColega:
        diferencaIdade = idadeColega - idadeUsuario
        print(f"A diferença de idade entre {nomeUsuario} e {nomeColega} é de {diferencaIdade} anos ")
    else :
        diferencaIdade = idadeUsuario - idadeColega
        print(f"A diferença de idade entre {nomeUsuario} e {nomeColega} é de {diferencaIdade} anos ")

#7
mediaIdade = (idadeUsuario * idadeColega)/2

print("A média da das idades de {} e {} é de {}".format(nomeUsuario, nomeColega, mediaIdade))


