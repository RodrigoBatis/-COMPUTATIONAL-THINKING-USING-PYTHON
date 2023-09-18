# def calcular_divisao():
#     while True:
#         message = ""
#         try:
#             num1 = int(input("Digite o numerador: "))
#             num2 = int(input("Digite o denominador: "))
#             div = num1 / num2
#         except ValueError:
#             message = "Os valores inputados não são numéricos"
#         except ZeroDivisionError:
#             message = "Impossivel dividir por zero."
#         else:
#             message = f"Divisão realizada com sucesso, valor {div}"
#             return div
#         finally:
#             print(message)
#             print()
#
# print(calcular_divisao())

# while True:
#     try:
#         num_1 = int(input("Digite o numero 1: "))
#         num_2 = int(input("Digite o numero 2: "))
#         div = num_1 / num_2
#     except ValueError:
#         print("Digite apenas caracteres númericos.")
#     except ZeroDivisionError:
#         print("Impossivel dividir com zero.")
#     else:
#         print(f"O valor da divisão de {num_1} por {num_2} é {div}")
#     finally:
#         print()
#
# def captura_numero(idx):
#     while True:
#         try:
#             num = int(input(f"Digite o numero {idx}: "))
#         except ValueError:
#             print("Digite apenas caracteres numéricos. ")
#         else:
#             return num
#         finally:
#             print()

