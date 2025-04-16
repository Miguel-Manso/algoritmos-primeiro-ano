#Escreva um programa que simule o jogo da "adivinhação" em que o computador escolhe um número aleatório e o usuário tem que tentar adivinhar o número. O programa deve continuar pedindo ao usuário para adivinhar até que ele acerte o número.
import random 
valor = random.randint(0, 20)
numUser = int

while valor != numUser:
    numUser = int(input("Tente adivinhar um numero entre 0 e 20: "))

print("Acertou")
