#Escreva um algoritmo que leia um número e informe se ele é
#divisível por 10, por 5 ou por 2 ou se não é divisível por nenhum deles

numero = int(input('Digite o seu número: '))
divisivel_dez = (numero / 10)
divisivel_cinco = (numero / 5)
divisivel_dois = (numero / 2)


if (numero < 10):
    print('Não é divisivel por 10')


elif (divisivel_dez.is_integer()):
    print('O seu número é divisível por 10')

else:
    print('Não é divisível por 10')

if (numero < 5):
    print('Não é divisivel por 5')

elif (divisivel_cinco.is_integer()):
    print('O seu número é divisível por 5')

else:
    print('Não é divisível por 5')

if (numero < 2):
    print('Não é divisivel por 2')

elif (divisivel_dois.is_integer()):
    print('O seu número é divisível por 2')

else:
    print('Não é divisível por 2')

