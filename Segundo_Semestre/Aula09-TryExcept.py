j1 = {
    'id': 1,
    'peso_mercadoria' : '20',
    'item': 'caixa 1'
}

j2 = {
    'id': 1,
    'peso_mercadoria' : 'vinte kilos',
    'item': 'caixa 1'
}

int(j1['peso_mercadoria'] * 1000)

try:
    j2['peso_mercadoria'] = int(j2['peso_mercadoria'])
except ValueError:
    print("Dados corrompido na chave peso_mercadoria")
except NameError:
    print("A chave peso_mercadoria não foi encontrada no dicionário")

