#A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. 
# Faça um algoritmos para coletar dados sobre o salário e número de filhos de cada habitante 
# e após as leituras, escrever: 
#Média de salário da população
#Média do número de filhos
#Maior salário dos habitantes
#Percentual de pessoas com salário menor que R$ 150,00

quantidade = int(input("Digite a quantidade de habitantes: "))
guardarSalario = 0
guardarFilho = 0
maiorSalario = guardarSalario
contadorSalario = 0

for i in range(quantidade):
    salario = float(input("Digite o salario do habitante: "))
    numFilho = float(input("Digite a quantidade de filhos do habitante: "))

    guardarSalario = guardarSalario + salario
    divisaoSalario = guardarSalario/quantidade

    guardarFilho = guardarFilho + numFilho
    divisaoFilhos = guardarFilho/quantidade

    if salario > maiorSalario:
        maiorSalario = salario

    if salario < 150:
        contadorSalario = contadorSalario + 1
    
    percentagem = (contadorSalario*100)/quantidade

print("A média salarial é :",divisaoSalario)  
print("A média de filhos é :",divisaoFilhos)
print("O maior salário é :",maiorSalario)
print("A percentagem de pessoas que recebem menos que 150 reais são: ", percentagem)
