## *ARGS e **KWARGS (KeyWord Args)
def print_formando(n):
    print(f"{n:.2f}")

def soma_dos_numeros(*args):
    soma=0
    for i in args:
        soma+=i
    return soma

soma=soma_dos_numeros(10,2,35,767,54,23,1,24,77);
print(soma)
print()

def cadastra_no_sistema(**Kwargs):
    print(Kwargs)

cadastra_no_sistema(nome="Rodrigo", idade=18)


## ARGUMENTOS PRÉ-DEFINIDOS










