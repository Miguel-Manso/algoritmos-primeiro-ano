"""Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve
ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o
valor zero e imprimir o resultado da divisão do primeiro valor lido pelo
segundo valor lido."""

num1 = float(input("Digite o primeiro número para ser realizado a divisão: "))
num2 = float(input("Digite o segundo número para ser realizado a divisão: "))

while num2 == 0:
    num2 = float(input("Digite um número diferente de zero: "))

divisao = num1 / num2

print("O resultado da divisão entre o primeiro e o segundo número é: ", divi