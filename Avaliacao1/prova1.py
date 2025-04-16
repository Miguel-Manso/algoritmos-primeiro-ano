#A prefeitura de Bebedouro abriu uma linha de crédito para os
#funcionários estatutários. O valor máximo da prestação não poderá ultrapassar
#30% do salário bruto. Fazer um algoritmo que permita entrar com o salário bruto
#e o valor da prestação, e informar se o empréstimo pode ou não ser concedido.
#O valor máximo não pode ultrapassar 30% do salário bruto


prestacao = float(input('Digite o valor da prestação: ')) 
salario = float(input('Digite o seu salário bruto: ')) 

percentagem = (30 / 100 * prestacao)
print('30% da sua prestação é: ', percentagem )

if percentagem > salario:
    print("Não pode fazer empréstimo")

else:
    print("Pode fazer empréstimo")
