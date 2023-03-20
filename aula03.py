# #Formatando numeros inteiros
num = 23
print(f"Número {num:5d}")
print(f"Número {num:05d}")
print(f"Número {num:>05d}")
print(f"Número {num:<05d}")
print(f"Número {num:^05d}")
#
# #Formatando Strings
nome = "FIAP"
print(f"Nome = {nome:>10s}")
print(f"Nome = {nome:>010s}")
print(f"Nome = {nome:*<10s}")
print(f"Nome = {nome:<10s}")
print(f"Nome = {nome:^10s}")
print(f"Nome = {nome:^010s}")
#
# #Formatando numeros float
Num_float = 12.0123456789
print('{:>10f}'.format(Num_float))
print('{:*<10f}'.format(Num_float))
print('{:.10f}'.format(Num_float))
print('{:.1f}'.format(Num_float))
print('{:*^10.2f}'.format(Num_float))
#
# #Manipulando String, formatando e salvando
#
Nome = "COMPUTATIONAL THINKING USING PYTHON"
Tamanho = len(Nome)
print(Tamanho)
Todas_maiusculas = Nome.upper()
print(Todas_maiusculas)
Todas_minusculas = Nome.lower()
print(Todas_minusculas)
Iniciais_maiusculas = Nome.title()
print(Iniciais_maiusculas)
Primeira_maiuscula = Nome.capitalize()
print(Primeira_maiuscula)

## Exercicios

# Exercício 1. Dado um numero pelo usuário, calcular o dobro e o quadrado
# obs: ao imprimir, colocar junto o número original

print("Dobro de 1 numero")
Numero    = float(input("Digite um numero:"))
Dobro = Numero * 2
Quadrado = Numero * Numero
print("Numero digitado {e} e o dobro desse numero é {r} e o quadrado é {t}".format(e=Numero, r = Dobro, t=Quadrado      ))
print()

# Exercício 2. Dados três números pelo usuário, calcular sua média,
# e a razão entre o primeiro e o último
# obs: definir a resposta a 10 caracteres, sendo 3 decimais

print("Média e razão de 3 numeros ")
Primeiro_numero    = float(input("Digite o primeiro numero:"))
Segundo_numero     = float(input("Digite o segundo  numero:"))
Terceiro_numero    = float(input("Digite o terceiro numero:"))
Media = (Primeiro_numero + Segundo_numero + Terceiro_numero)/3
Razao = Primeiro_numero / Terceiro_numero
print("A media dos numeros digitados é {:10.3f}".format(Media))
print("A razão entre o primeiro e o terceiro numero é {:10.3f}".format(Razao))
print()

# Exercício 3. Dado um numero pelo usuário, exibir o anterior e posterior
# (Ex: input=20, resposta=19 e 21)

print("Mostrando o anterior e o proximo de 1 numero")
Numero    = float(input("Digite um numero:"))
Proximo_numero = Numero + 1
Numero_anterior = Numero - 1
print("Numero digtado {e} proximo numero {r} e o numero posterior dele {t}"
      .format(e = Numero, r = Proximo_numero, t = Numero_anterior ))
print()

# Exercício 4. Dados dois numeros pelo usuário, calcular a potência entre eles

print("Potência de dois numeros")
Primeiro_numero    = float(input("Digite o primeiro numero:"))
Segundo_numero     = float(input("Digite o segundo  numero:"))
Potencia = Primeiro_numero ** Segundo_numero
print("A potência dos numeros digitados é {}".format(Potencia))
print()

# Exercício 5. Dado um numero pelo usuário, exibir o proximo multiplo de 5

print("Mostrando o anterior e o proximo multiplo de 5 do numero digitado")
Numero    = float(input("Digite um numero:"))
Falta_para_chegar_em_multiplo_de_5 = Numero // 5
Proximo_multiplo = Falta_para_chegar_em_multiplo_de_5 * 5 + 5
print("Proximo multiplo de 5 do numero {} é {}".format(Numero, Proximo_multiplo))
print()