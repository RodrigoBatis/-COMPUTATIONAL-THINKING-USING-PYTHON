### Ordenando  a lista
l=[5,1,3,7,4,9]

print(l.sort())
print(l)
print()

lista=[5,1,3,7,4,9]
lista_ordenada = sorted(lista)
print(lista)
print(lista_ordenada)
print()

lista.reverse()
print(lista)
print()

##Extend e +
#Para adicionar mais de um item por vez na lista
lista=[]
lista.extend([5,5])
print(lista)
print()

## Inserir um novo item na lista com insert é só pegar o indice que quer colocar e o item
lista=[1,2,3,4,5]
lista.insert(2,6)
print(lista)
print()

print("-------------------------------")
#Vamos remover todos os '5'
i=0
lista = [1,5,7,5,5,9,6,87,5,5]
lista_copy = lista.copy()
print(f"Lista antes de ser alterada {lista}")
print()
while i <= len(lista):
    if lista[i] == 5:
        lista_copy.remove(5)
        print("Lista após remoção: ", lista_copy)
    i+=1
print(f"Lista resultado final {lista_copy}")



