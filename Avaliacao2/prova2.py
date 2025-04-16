"""Utilizando o código do exercício anterior, ler
dois valores (considere que não serão
lidos valores iguais) e escrevê-los em ordem crescente.

""" 

Num1 = float(input("Digite o seu primeiro número para saber se é maior que o segundo por meio de uma ordem crescente: "))
Num2 = float(input("Digite o seu segundo número: "))

if Num1 > Num2:
    print(Num1)
    print(Num2)

elif Num1 == Num2:
    print("Os dois números são iguais.")

else:
    print(Num2)
    print(Num1)
