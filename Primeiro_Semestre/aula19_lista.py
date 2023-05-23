# AULA SOBRE LISTAS
# criando uma lista vazia:
lista1 = []
# criando uma lista com itens:
lista2 = [1,5,9]

#Adicionando um elemento na lista: (ao final da lista)
#Append
print()
print("----------------------------------------")
print("Adicionando um elemento na lista: (ao final da lista)")
print("Append")
print(lista1)
lista1.append(1)
print(lista1)
lista1.append(5)
lista1.append("String")
lista1.append(lista2)
print(lista1)
# lista1.append([2,3,4])
print(lista1)
print("----------------------------------------")

print()
print("----------------------------------------")
print("Lista1[1] antes da alteração: ",lista1[1])

#Alterando itens da lista:
#localizar pelo indice e alterar
lista1[1]=9
print("Lista1[1] após alteração: ", lista1[1])
print("----------------------------------------")

#Tamanho da lista = len(lista)
print()
print("----------------------------------------")
print("Tamanho da lista = len(lista)")
print("A lista 1 tem {} itens".format(len(lista1)))
print("----------------------------------------")

#pegando o último item utilizando o len
print()
print("----------------------------------------")
print("pegando o último item utilizando o len")
print(lista1[len(lista1)-1])
print("----------------------------------------")

#Acessar partes de lista(slices)
print()
print("----------------------------------------")
print("Acessar partes de lista(slices)")
print(lista1[0:2])
print("----------------------------------------")
print()

#Se eu tiver apenas numéricos,
# posso utilizar o sum(lista) para somar todos os valores

print("----------------------------------------")
print("Se eu tiver apenas numéricos,")
print("posso utilizar o sum(lista) para somar todos os valores")
lista_numeros=[5,7,94,5,.85,7956]
print(sum(lista_numeros))
print("----------------------------------------")
print()

#se eu quiser a média dos números da lista:
print("----------------------------------------")
print("se eu quiser a média dos números da lista:")
media_da_lista = sum(lista_numeros)/len(lista_numeros)
print(media_da_lista)
print("----------------------------------------")
print()

print("----------------------------------------")
lista=[1,2,3,9,4,5,6]
print("Lista original: ", lista)

##Retirando itens da lista: temos 2 opções
print("Retirando itens da lista: temos 2 opções:")
print()
### .pop(), onde escolhermos o Índice
##  .pop() retorna o valor retirado
print(".pop(), onde escolhermos o Índice")
print(".pop() retorna o valor retirado")
valor_retirado = lista.pop(1)
print(f"{valor_retirado} foi retirado da lista {lista}")

### .remove(), onde escolhemos o Valor
##  .remove()
print()
print(".remove(), onde escolhemos o Valor")
print(".remove()")
lista.remove(9)
print("lista após remove(9): ", lista)
print("----------------------------------------")
print()

print("----------------------------------------")
lista = [1,5,7,5,5,9,6,87,5,5]
lista_reserva = lista.copy()
print("Lista completa: ", lista)

#Vamos remover todos os '5'
for i in range(len(lista)):
    print("Interação: ", i)
    print("Avaliação atual", lista[i])
    print()
    if lista[i] == 5:
        lista_reserva.remove(5)
        print("Lista após remoção: ", lista_reserva)

print()
print("Lista Após todos os deletes: ", lista_reserva)
