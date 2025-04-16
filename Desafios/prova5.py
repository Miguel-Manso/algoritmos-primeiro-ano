#Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km.
#  Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45 
# para viagens mais longas.

numDistancia = float(input("Digite a distância que desejas percorrer em Km: "))

if numDistancia < 200:
    print(numDistancia*0.50)

else:
    print(numDistancia*0.45)

