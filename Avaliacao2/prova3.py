"""Escreva um algoritmo para ler 10 números e ao
final da leitura escrever a soma total dos 10 números lidos.
 """

soma = 0

for i in range(10):
    num = float(input("Digite o número: "))
    soma += num

print (soma)
   
