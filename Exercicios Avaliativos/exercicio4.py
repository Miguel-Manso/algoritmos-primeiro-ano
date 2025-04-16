#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá
#se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos
#cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na
#tela.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = (numero1 + numero2)
multi = (numero1 * numero2)

if numero1 == numero2:
    print('A soma é: ', soma)

else:
    print('A multiplicação é: ', multi)