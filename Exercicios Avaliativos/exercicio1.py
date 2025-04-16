#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é
#menor que C.
n1 = float(input('Digite o número 1: ')) 
n2 = float(input('Digite o número 2: ')) 
n3 = float(input('Digite o número 3: ')) 

soma = (n1 + n2)

if soma < n3:
    print('A soma é menor que o número 3')
