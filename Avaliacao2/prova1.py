""" Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior
deles.
"""

Num1 = float(input("Digite o seu primeiro número para saber se é maior que o segundo: "))
Num2 = float(input("Digite o seu segundo número: "))

if Num1 > Num2:
    print("O primeiro número é maior: ", Num1)
elif Num1 == Num2:
    print("Os dois números são iguais.")
else:
    print("O segundo número é maior: ", Num2)

