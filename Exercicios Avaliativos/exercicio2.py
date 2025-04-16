#Faça um algoritmo que leia o nome, o sexo e o estado civil (M ou F) de uma pessoa.
#Caso o estado civil seja “CASADA(o)”, solicitar o tempo de casada(o) em (anos) e o
#nome do companheiro(a) e exibir o nome da pessoa, o tempo de casada e o nome do
#companheiro.



nome = input('Digite o seu nome: ') 
sexo = input('Digite o seu sexo entre M e F: ') 
estadoCivil = input('Digite seu estado civil: ') 

if estadoCivil == 'casada' or estadoCivil == 'casado':
    tempoCasamento = float(input('Digite o seu tempo de casamento em anos: '))
    nomeCompanheiro = (input('Digite o nome do seu companheiro: '))

    print(nome)
    print(tempoCasamento)
    print(nomeCompanheiro)

else:
 print('Fim')