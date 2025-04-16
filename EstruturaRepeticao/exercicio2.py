##Utilizando a estrutura de repetição for, faça um programa em python que receba 10 números e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.

import random
for i in range(10):
    valor = random.randint(0, 100)
    if valor > 10 and valor < 20:
        print("Está entre 10 e 20: ", valor)
    else:
        print("Está fora de 10 e 20: ", valor)
    
