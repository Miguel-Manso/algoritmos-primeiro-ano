#A sequência de Fibonacci tem papel importante na explicação
#de fenômenos naturais. Ela é também bastante utilizada para fins estéticos, pela
#sua reconhecida harmonia. Exemplo disso foi sua utilização na construção do
#Partenon, em Atenas. A sequência dá-se inicialmente por dois números 1. A
#partir do terceiro elemento usa-se a expressão: elemento n = elemento n1 + elemento n2. 
# Exemplo de sequência: 1, 1, 2, 3, 5, 8. Construa um
#algoritmo que imprima na tela os 10 primeiros elementos da sequência de
#Fibonacci

primeiro = 1
segundo = 1


for i in range (1, 2):
    print(i)
    print(i)


for i in range(8):
        conta = primeiro + segundo
        segundo = primeiro
        primeiro = conta
        print(conta) 
   
      
    
        