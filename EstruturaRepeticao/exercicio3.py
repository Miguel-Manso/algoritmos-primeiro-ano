# Escreva um programa que peça ao usuário para digitar um número inteiro positivo e, em 
# seguida, exiba todos os números ímpares de 1 até esse número.

numero = int(input('Digite o seu número inteiro e positivo: '))

if numero < 1:
    print('Recomeçe')

for i in range (1, numero):
    if i % 2 == 1:
        print(i)
