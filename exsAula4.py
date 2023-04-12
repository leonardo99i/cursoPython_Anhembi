'''
Considere a lista a seguir como a quantidade de itens vendidos por cada vendedor de uma loja.
vendas = [100, 150, 1500, 2000, 120]
Caso o vendedor tenha vendido mais de 1000 unidades, ele ganha um bônus de 15% sobre seu salário.
Fazer um programa que informa quem conseguiu o bônus.
'''

vendas = [100, 150, 1500, 2000, 120]
bonus = 0.15

print("Central de Vendas:")

for i in range(len(vendas)):
    if vendas[i] > 1000:
        print(f"Vendedor {i+1} conseguiu o bonus de {bonus*100}% sobre o salario.")