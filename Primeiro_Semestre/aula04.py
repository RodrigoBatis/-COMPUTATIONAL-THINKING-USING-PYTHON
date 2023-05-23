## Calcular a autonomia do automóvel do usuario
'''
definir que a autonomia seria em km/l
solicitando ao usuario a quantidade de km percorridos
solicitar ao usuario a volume de combustivel gasto (em L) para percorrer esta distancia
converte (casting) e faz a conta
retorna ao usuario a autonomia de seu veiculo
'''

## Calcular o custo mensal com combustivel do usuario
'''
--> já posuiamos a autonomia do automovel do usuario (em km/l)
(frequencia de abastecimento  "3")
solicitar ao usuario a media de km rodados por dia util
transformar a média diaria em média mensal
calcular o consumo em L medio no mes -> 

    15km    ->      1L
    800km   ->      XL
    
    15X = 800
    X = 800/15
    X = 53.3L
    
OU solicitar ao usuario o preço que ele pagou por litro
OU buscar em bancos de dados/fontes externas
temos que o preço do litro de gasolina é R$5,00

multiplicar o preço pela quantidade consumida
'''

autonomia_em_km_por_L = 15
media_km_por_dia = float(input("Digite a média de km que você percorre por dia útil: "))

media_km_mensal = media_km_por_dia * 20
media_litros_por_mes = media_km_mensal/autonomia_em_km_por_L

preco_por_litro = float(input("Diga quando você pagou em reais por litro de gasolina (OBS: sem R$): "))

valor_gasto_mensal = media_litros_por_mes * preco_por_litro

print("Você gasta, em média, por mês R${:.2f} com combustível".format(valor_gasto_mensal))



