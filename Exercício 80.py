#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
#Já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

import time

print("Iremos montar um programa que você digitará cinco valores, numa lista")
time.sleep(1)
print("Iremos colocar já na posição correta sem usar sort")
time.sleep(1)

lista = []
replace = []

for C in range(0,5):
    n = int(input("Digite um número: "))
    lista.append(n)
    time.sleep(1)

if C == 0 or n > lista[-1]:
    lista.append(n)    
else:
    pos = 0
    while pos < len(lista):
        if n <= lista[pos]:
            lista.insert(pos, n)
            break
        pos += 1
print(lista)
        



print(lista)
