#Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
#decrescente.

n1 = int(input('Digite o número 1: ')) 
n2 = int(input('Digite o número 2: ')) 
n3 = int(input('Digite o número 3: ')) 

if n1 == n2 and n1 == n3 or n2 == n3:
    print('Há números semelhantes. Recomeçe')

##Maior
if n1 > n2 and n1 > n3:
    maior = n1

elif n2 > n1 and n2 > n3:
    maior = n2

else:
    maior = n3

##Menor
if n1 < n2 and n1 < n3:
    menor = n1

elif n2 < n1 and n2 < n3:
    menor = n2

else:
    menor = n3

##Meio
meio = n1 + n2 + n3 - maior - menor

print(maior, meio, menor)