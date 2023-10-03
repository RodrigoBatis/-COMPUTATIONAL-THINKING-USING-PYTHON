# Considere todo o conteúdo visto até o momento.

#################################################
#########           Desafio             #########
#################################################

# Utilize a biblioteca python requests para o consumo das API's
# Considere a PokéAPI (api com dados dos pokemons)
# https://pokeapi.co/docs/v2
# Não se esque de incluir tratativas de exceções.

# Questões
# Parte 1: Crie uma função que dado o nome ou id de um pokemon
# retorne um dicionário com seus atributos da forma:
# {
#     "abilities": [nome_de_todas_as_habilidades],
#     "forms": [nome_de_todas_as_formas],
#     "height": <numero>,
#     "id": pokemon_id,
#     "name": name,
#     "weight": peso_do_pokemon
# }
# Exemplos:
#   - consultar o pokemon bulbasaur: https://pokeapi.co/api/v2/pokemon/bulbasaur
#   - consultar o pokemon ivysaur: https://pokeapi.co/api/v2/pokemon/ivysaur
#   - consultar o pokemon charmander: https://pokeapi.co/api/v2/pokemon/charmander
#
# Caso haja um erro, como pokemon inexistente,
# gere uma exceção CUSTOMIZADA com a mensagem correspondente
# Exemplo de erro: https://pokeapi.co/api/v2/pokemon/10000 => retorna 404

class ErroListaGet(Exception):
    ...


import requests
import pprint

base_url = "https://pokeapi.co/docs/v2"

def consultaPokemonIdOuNome(nome_id):
    url = f"{base_url} /pokemon/{nome_id}"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        return data
    raise ErroListaGet(f"Falha na listagem do get por id ou nome {nome_id} error {response.status_code}")

if response.status_code == 200:
    data = response.json()
    for pokemon in data:
        user_id = user["id"]
        user_name = user['name']

# Parte 2: Crie uma função que dado uma string,
# valide se essa string corresponde a um CPF válido.
# As regras para validação de um CPF são:
# - Conter 11 dígitos
# - Validar os dígitos verificadores,
#       como descrito em: https://www.calculadorafacil.com.br/computacao/validar-cpf
# Você ainda deverá aceitar os formatos:
# - Com pontos e traços (xxx.xxx.xxx-xx)
# - Sem pontos e traços (xxxxxxxxxxx)
#
# Caso o CPF seja inválido, gere uma exceção CUSTOMIZADA, com a mensagem correspondente.
#   Casos obrigatórios:
#       - Exceção para formato inválido
#           - deverá contemplar os casos de caracteres não permitidos,
#               além do tamanho (número de dígitos) menor ou maior que o especificado.
#       - Exceção para dígitos inválidos
#           - deverá ocorrer quando não obedecer a regra de validação.
# Exemplo de CPF inválido: 111.111.111-11
# Exemplo de CPF válido:   377.136.110-96


# Parte 3: Crie uma função que calcule o Pokemon id de uma pessoa, dado um CPF VÁLIDO:
# O Pokemón id será calculado utilizando a seguinte função de hash:

# def poke_hash(cpf: int) -> int:
#     # Note que a variável cpf deverá ter sido convertida para inteiro
#     # ANTES de chamar a função poke_hash
#     return cpf % 97


# Utilize a validação de CPF.
# Sua função deverá ser robusta a erros da função de validação de CPF,
# tratando exceções, mas não às escondendo.
# Dica:
# try:
#     raise Exception("oi, eu sou o Goku")
# except Exception as e:
#     print("\nHouve um exception.\n")
#     raise e

# Parte 4: crie um Menu que ofereça ao usuário as opções:
# - Opção 1: Consultar os dados de um Pokemon
#   -> solicite o id ou nome do pokemon
#   -> nesta opção, utilize a biblioteca pprint para a impressão no terminal
#       Dica: pprint.pprint(TEXTO)
#
# - Opção 2: Consultar qual seu pokemon
#   -> nesta opção, peça o CPF do usuário
#       e reutilize as funções desenvolvidas nas questões 2 e 3.
#   -> imprima os dados com pprint, assim como no item anterior.
#
# - Opção 3: Encerrar ou continuar a execução, para isso:
#   -> utilize um loop infinito
#   -> solicite a confirmação com s/N:
#         -> aceite diferentes casos como: "sim", "s", "Sim", "n", etc...
#
# Você deverá tratar todas as execeções que possam ser geradas dentro das funções anteriores
