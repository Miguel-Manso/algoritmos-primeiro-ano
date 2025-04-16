"""Acrescentar uma mensagem de 'VALOR INVÁLIDO' no exercício anterior caso o segundo valor informado 
seja ZERO.
"""
num1 = float(input("Digite o primeiro número para ser realizado a divisão: "))
num2 = float(input("Digite o segundo número para ser realizado a divisão: "))

if num2 == 0:
    print("VALOR INVÁLIDO!") 

else:
    divisao = num1 / num2

    print("O resultado da divisão entre o primeiro e o segundo número é: ", divisao)
