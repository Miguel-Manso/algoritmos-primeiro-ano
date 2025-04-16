#Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever:
#o maior preço lido
#a média aritmética dos preços dos produtos

num = 0
maiorValor = num

for i in range (15):
    valor = int(input("Digite o preço do seu produto: "))

    if valor > maiorValor:
        maiorValor = valor

    num = num + valor
    divisao = num/15
    
print(divisao)
