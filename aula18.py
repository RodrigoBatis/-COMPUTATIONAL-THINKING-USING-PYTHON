# def verifica_par(numero):
#     return numero%2==0
#
# def verifica_positivo(numero):
#     return numero >=0
#
# n=float(input("Diga um número positivo e par"))
# while True:
#     if verifica_par(n) and verifica_positivo(n):
#         break
#     else:
#         n = float(input("Diga um número positivo e par"))

# def soma_e_multiplica(condicao,*args):
#     soma = 0
#     multi = 1
#     for i in args:
#         soma+=i
#         multi *= i
#
#     return soma, multi, args
#
# soma, produto, numeros_digitados = soma_e_multiplica(10,10,10)
# print(f"Soma dos valores {numeros_digitados} é {soma}")
# print(f"Multiplicação dos valores {numeros_digitados} é {produto}")

# def soma_e_multiplica(condicao, *args):
#     if condicao == "soma":
#         soma = 0
#         for i in args:
#             soma += i
#         return soma
#     elif condicao == "multiplicar":
#         multi = 1
#         for i in args:
#             multi *= i
#         return multi
#
# result_funcao = soma_e_multiplica("multiplicar", 10, 10, 10)
# print(result_funcao)

def esta_entre(n, maior, menor):
    return menor < n < maior


