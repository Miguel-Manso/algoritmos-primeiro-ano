#Escreva um programa que gere a sequência de Fibonacci até um determinado limite fornecido pelo usuário. A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma dos dois números anteriores.

numUser = int(input("Digite o Limite para a sequência de Fibonacci: "))
primeiroNum = 0
segundoNum =  1
novoNum = 1


while novoNum <= numUser:
    print(novoNum)
    novoNum = primeiroNum + segundoNum
    primeiroNum = segundoNum
    segundoNum = novoNum
