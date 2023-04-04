# for i in range(5):
#     print(f"Numero {i}")
#     print(f"Dobro do numero {i*2}")
#     if i%2==0:
#         print("Numero é par")
#     else:
#         print("Numero é impar")
#     print("------------------------")

# Para cada numero de 0 a 4, imprima a soma dos anteriores (positivos)

# soma = 0
# for i in range(5):
#     print(soma)
#     soma+=i

print("---------------")

numeroAtual = 1
numeroAnterior = 0
for i in range(3,5):
    soma = numeroAnterior + numeroAtual
    numeroAnterior= numeroAtual
    numeroAtual=soma
print(numeroAtual)


