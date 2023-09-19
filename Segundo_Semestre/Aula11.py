# 1 - Calculadora de Idade com Tratamento de Data de Nascimento:
# PeÃ§a ao usuÃ¡rio para inserir sua data de nascimento no formato "dd/mm/aaaa".
# Utilize try, except para capturar erros de entrada e calcular a idade da pessoa.
# Em seguida, use um bloco else para exibir a idade calculada e um bloco finally
# para agradecer ao usuÃ¡rio por usar a calculadora.

from datetime import datetime

class DataInvalidaError(ValueError):
    ...

now = datetime.now()
while True:

    try:
        data_nascimento = input("Digite a sua data de nascimento no formato dd/mm/yyyy: ")
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        if data_nascimento > now:
            raise ValueError
    except DataInvalidaError:
        print(DataInvalidaError)
        raise ValueError
    except ValueError:
        print("Data inválida. Atente-se ao formato dd/mm/yyyy.")
        print("Tente novamente")
        print()
    except KeyboardInterrupt:
        ...
    else:
        idade = (now- data_nascimento).days // 365
        print(f"Sua idade é {idade}")
        print()
    break

print("Obrigado pro utilizar a calculadora")

# API intro
# exemplo https://www.google.com.br/search?q=

# registro = [{....}]
#
# def search(q):
#     for registro in registros:
#         if q in registro.keys():
#             return registro
