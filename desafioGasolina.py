'''
Um posto de gasolina está vendendo combustíveis com a seguinte tabela de descontos: 

Gasolina:
Até 20 litros: desconto de 4% por litro
Acima de 20 litros: desconto de 6% por litro

Álcool:
Até 20 litros: desconto de 3% por litro
Acima de 20 litros: desconto de 5% por litro

Escreva um programa que leia o tipo de combustível (A - Álcool e G - Gasolina),
calcule e imprima o valor a ser pago pelo cliente.

PARA TORNAR O DESAFIO INTERESSANTE, VAMOS FAZER O PROGRAMA CRIAR UM NÚMERO 
ALEATÓRIO PARA O ABASTECIMENTO. ESTE NÚMERO DEVERÁ SER ENTRE 1 E 52
'''
import random

combustivel = input("Digite o tipo de combustível (A - Álcool e G - Gasolina): ")
litros = random.randint(1, 52)

preco_gasolina = 5.39
preco_alcool = 4.29

if combustivel == "G":
    if litros <= 20:
        preco = litros * (preco_gasolina * 0.96)
    else:
        preco = litros * (preco_gasolina * 0.94)
else:
    if litros <= 20:
        preco = litros * (preco_alcool * 0.97)
    else:
        preco = litros * (preco_alcool * 0.95)

print(f"Abasteceu {litros} litros de {combustivel}, totalizando R${preco:.2f}")

