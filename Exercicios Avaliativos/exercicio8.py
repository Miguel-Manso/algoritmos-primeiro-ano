""" 
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
para homens: (72.7 * h) – 58;
para mulheres: (62.1 * h) – 44.7. 10)
O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para
dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC =
peso / ( altura )2
Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição
de acordo com a tabela abaixo. IMC em adultos Condição
Abaixo de 18,5 Abaixo do peso
Entre 18,5 e 25 Peso normal
Entre 25 e 30 Acima do peso
Acima de 30 obeso
"""
##peso
sexo = input("Sexo (M ou F): ")
alturaInicial = float(input("Altura: "))

if sexo == "M":
    pesoMasculino = (72.7*alturaInicial)-58
    print(pesoMasculino)
elif sexo == "F":
    pesoFeminino = (62.1 *alturaInicial) - 44.7
    print(pesoFeminino)
else:
    print("Sexo nao identificado")

##Parte IMC
peso = float(input("Seu peso: "))
altura = float(input("Sua Altura: "))

imc = peso/(altura * altura)
if imc < 18.5:
    print('Abaixo do peso', imc)
    
elif imc < 26:
    print('Peso normal', imc)
    
elif imc < 30:
    print('Acima do peso', imc)
    
else:
    print('Obeso', imc)
