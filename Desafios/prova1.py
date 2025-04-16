#Faça um programa que leia 15 valores e no
#final, escreva o maior e o menor valor lido.
num1 = int(input("Digite o número: "))
numMaior = num1
numMenor = num1

for i in range(14):
    

    num1 = int(input("Digite o número: "))
    if num1 < numMenor:
        numMenor = num1


    elif num1 > numMaior:
        numMaior = num1

print("O maior número é: ", numMaior)
print("O menor número é: ", numMenor)
