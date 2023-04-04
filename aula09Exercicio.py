'''4)	Solicite ao usuário (separadamente) o mês do ano, e o dia atual.
 Diga em qual estação estamos
ex: 28 de março -> primeiro input = 3, segundo input = 28
Outono : De 22 de março a 21 de junho.
Inverno: De 22 de junho a 23 de setembro.
Primavera: De 24 de setembro a 21 de dezembro.
Verão: De 22 de dezembro a 21 de março.

similar ao das notas, só que agora cada mês tem mais condições
'''

mes = input("Digite o nome do mês do ano que está(completo): ").upper()
dia = int(input("Digite o dia do mês que está: "))

if mes == "JANEIRO" or mes == "FEVEREIRO" :
    print("A estação do ano é Verão!!")
elif mes == "MARÇO":
    if dia <= 21:
        print("A estação do ano é Verão!!")
    else:
        print("A estação do ano é Outono!!")






