#Construa um algoritmo que indique se um número digitado está
#compreendido entre 20 e 90 ou não (20 e 90 não estão na faixa de valores)

numero = float(input('Digite o seu número: '))

if numero in range(20, 91):
    print("Está na faixa")

else:
    print('Não está na faixa')
