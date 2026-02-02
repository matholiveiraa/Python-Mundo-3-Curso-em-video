#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
import random
import time


numeros = []

for C in range(5):
    C = random.randint(1,30)
    numeros.append(C)

print(f"Lista: {numeros}")
print(f"Maior valor gerado: {max(numeros)}")
print(f"Menor valor gerado: {min(numeros)}")




