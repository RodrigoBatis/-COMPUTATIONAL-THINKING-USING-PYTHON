#EXERCÍCIOS:

#1) Crie uma função que receba um número inteiro positivo N como parâmetro
# (e que por padrão seja =1) e retorne um dicionário cujas chaves
# são os números de 0 até N, e os valores, seus quadrados
# ex: N=3, dict={0:0,1:1,2:4,3:9}

# dict = {n:n**2}

def n_quadrados(N=1):  
   
   # dicio = {}

   # for n in range(N+1):
   #     dicio[n] = n**2

   dicio = {n:n**2 for n in range(N+1)} #A mesma que a da cima só que comprimida

   return dicio  

dicio_ex_1 = n_quadrados()

print(dicio_ex_1)
print()

#2) Crie uma função que receba um dicionário e some e retorne
# seus valores numéricos
# Caso não exista nenhum, deverá imprimir uma mensagem de erro

dicio_ex_2={}

def soma_valores_dicio(dicio_ex_2):
   resposta = 0
   validador = True
   for valor in dicio_ex_2.values():
      if type(valor) == int or type(valor) == float:
         resposta += valor
         validador = False
   if validador:
      return "ERRO! Não possui valores numéricos"
   return resposta

resposta_final = soma_valores_dicio(dicio_ex_2)
print(resposta_final)
print()
      

#3) Transforme duas listas de tamanhos iguais e um dicionário
# ex: [1,2] e ["um","dois"] viram {1:"um",2:"dois}

lista1= ["cor", "tampa"]
lista2= ["preta", "branca"]
dicio={}
for i in range(len(lista1)):
   dicio[lista1[i]] = lista2[i]

dicio2=dict(zip(lista1, lista2)) ## Possui a mesma função da anterior de forma resumida

print(dicio)
print(dicio2)
print()


#4) faça uma função que recebe um dicionário e
# qualquer número de chaves, e retorne um novo dicionário contendo
# apenas estas chaves(ou seja, que filtre um dicionario)
# ex: dict1={"nome": "Fulano","idade": 25,"cidade": "Rio de Janeiro"}
#     chave = "nome"
#    retorno = {"nome":Fulano}
dict1={"nome": "Fulano","idade": 25,"cidade": "Rio de Janeiro"}

dicio = {chave:valor for chave,valor in dict1.items() if chave == "nome"}
print(dicio)
