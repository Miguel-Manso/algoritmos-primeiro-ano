#Faça um algoritmo para ler uma quantidade e a
#seguir ler esta quantidade de números. Depois de ler todos os números o
#algoritmo deve apresentar na tela o maior dos números lidos e a média dos
#números lidos.

quantidade = int(input("Digite a quantidade de números que serão lidos: "))
num = 0
maiorValor = num


for i in range(quantidade):
    valor = int(input("Digite o número: "))

    num = num + valor
    divisao = num/quantidade

    if valor > maiorValor:
         maiorValor = valor

    

print("O maior número é: ", maiorValor)
print("A divisão é: ", divisao)
