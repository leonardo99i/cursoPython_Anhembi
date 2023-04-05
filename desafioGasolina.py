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

preco_gasolina_sem_desc = 5.69
preco_alcool_sem_desc = 4.49

if combustivel == "G":
    if litros <= 20:
        preco_desc = litros * (preco_gasolina_sem_desc * 0.96)
        preco_sem_desc = litros * preco_gasolina_sem_desc
    else:
        preco_desc = litros * (preco_gasolina_sem_desc * 0.94)
        preco_sem_desc = litros * preco_gasolina_sem_desc
else:
    if litros <= 20:
        preco_desc = litros * (preco_alcool_sem_desc * 0.97)
        preco_sem_desc = litros * preco_alcool_sem_desc
    else:
        preco_desc = litros * (preco_alcool_sem_desc * 0.95)
        preco_sem_desc = litros * preco_alcool_sem_desc

economia = preco_sem_desc - preco_desc

print(f"Abasteceu {litros} litros de {combustivel}")
print(f"Preço sem desconto: R${preco_sem_desc:.2f}")
print(f"Preço com desconto: R${preco_desc:.2f}")
print(f"Economia: R${economia:.2f}")
