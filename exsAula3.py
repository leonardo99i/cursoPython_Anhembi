'''
Meta de vendas: 50.000 unidades.
Usuário vai informar quantas unidades do produto foram vendidas.

Se a meta não for atingida, o programa deverá informar que a meta não 
foi atingida e ninguém recebe bonus.
Se a meta for atingida com menos de 500 unidades de diferença, o programa informa 
que a meta foi atingida e que os vendedores ganharão 5% de bonus.
Se a meta for ultrapassada em mais de 500 unidades, os vendedores receberão bonus de 15%.
'''

meta = 50000

totalVendas = int(input("Informe a quantidade de unidades vendidas: "))

if(totalVendas < meta):
    print("Meta não atingida, não existe bonus!")

elif totalVendas <= meta + 500:
    bonus = totalVendas * 0.05
    print(f"A meta foi atingida com uma diferença de 500 unidades. Os vendedores ganham um bonus de 5%. Total de bônus: R${bonus:.2f}")

else:
    bonus = totalVendas * 0.15
    print(f"A meta foi ultrapassada em mais de 500 unidades! Os vendedores receberão 15% de bônus. Total de bônus: R${bonus:.2f}")