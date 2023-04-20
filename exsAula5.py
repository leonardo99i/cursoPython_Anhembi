'''
Uma locadora de veículos possui o dicionário abaixo em seu estoque. 
Neste dicionário, podemos encontrar o veículo e o valor do aluguel por dia.

carros = {"Chevrolet Tracker": 120, "Chevrolet Onix": 90, "Hyundai HB20": 85, "Hyundai Tucson": 120, "Fiat Uno": 60, "Fiat Mobi": 70), "Fiat Pulse": 130)}

Faça um programa que um operador consiga verificar o estoque, retirar o veículo do estoque para locação informando: 
Veículo e tempo de locação e devolver o valor total da locação e, também, o operador deve conseguir inserir o veículo de volta ao estoque. 

'''

carros = {"Chevrolet Tracker": 120, "Chevrolet Onix": 90, "Hyundai HB20": 85, "Hyundai Tucson": 120, "Fiat Uno": 60, "Fiat Mobi": 70, "Fiat Pulse": 130}

while True:
    print("|-------------------------------|")
    print("|       ----- MENU -----        |")
    print("|1 - Verificar o estoque        |")
    print("|2 - Retirar veículo do estoque |")
    print("|3 - Inserir veículo no estoque |")
    print("|4 - Sair do Menu               |")
    print("|-------------------------------|")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        print("Estoque:")
        for veiculo, valor in carros.items():
            print(f"{veiculo}: R${valor}/dia")
    
    elif opcao == 2:
        veiculo = input("Digite o nome do veículo a ser alugado: ")
        dias = int(input("Digite o número de dias de locação: "))
        if veiculo in carros:
            valor_total = carros[veiculo] * dias
            del carros[veiculo]
            print(f"O veículo {veiculo} foi retirado do estoque por {dias} dias. Valor total da locação: R${valor_total}")
        else:
            print("Veículo não encontrado no estoque.")
    
    elif opcao == 3:
        veiculo = input("Digite o nome do veículo a ser inserido no estoque: ")
        valor = int(input("Digite o valor de locação por dia: "))
        carros[veiculo] = valor
        print(f"O veículo {veiculo} foi inserido no estoque com valor de locação de R${valor}/dia.")
    
    elif opcao == 4:
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Digite novamente.")
