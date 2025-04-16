#Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja
#ímpar, imprimir o resultado desta operação.

numero = int(input('Digite o seu número: '))

if (numero % 2) == 0:
    print('O seu numero somado a 5 é:', numero + 5)

else:
    print('O seu número somado a 8:', numero + 8)