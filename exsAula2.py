'''
 - Caluladora de Peso Ideal - 

Fazer uma calculadora em python que o usuário digita Altura em metros e Peso em quilos 
e se é do sexo biológico Masculino ou Feminino. O programa devolve ao usuário
a informação qual seu peso ideal e quando precisa emagrecer para chegar lá. 
Ao final, o programa deve trazer uma frase motivadora para aqueles que estão 
acima do peso, frase parabenizando os que estão no peso ideal e uma outra frase de 
alerta aos que estão abaixo do peso.

Fórmulas
>Masculino: (72.7 * Altura) - 50
>Feminino: (62.1 * Altura) - 44.7
'''

def pesoIdeal(altura, sexo):

    if(sexo == 'M'):
        return (72.7 * altura) - 50
    
    elif(sexo == 'F'):
        return (62.1 * altura) - 44.7
    
    else:
        return "Erro, indique M ou F para o sexo"
    

altura = float(input('Informe a sua altura em Metros. Ex: 1.75: '))
peso = float(input('Informe o seu peso em Quilos. Ex: 85: '))
sexo = str(input('Informe o sexo com M para Masculino ou F para Feminino: '))

resultado = pesoIdeal(altura, sexo)

print(f"Seu peso ideal é: {resultado:.1f} Kg")

if(peso > resultado):
    print("Você está acima do peso ideal, mas não desista você consegue")
elif(peso < resultado):
    print("Você está abaixo do peso ideal, um pouco de trabalho e você consegue, não desista")
else:
    print("Uallll você está dentro do seu peso ideal, muito bom continue assim")