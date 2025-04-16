#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja
#negativo, imprimindo o resultado.

numero = float(input('Digite o seu número: '))

if numero >= 0:
    print('O dobro do seu número é', numero * 2)

else:
    print('O triplo do seu número é', numero * 3)