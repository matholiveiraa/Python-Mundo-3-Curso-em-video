#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

import time
import heapq #bibilioteca para puxar 3 valores maiores


print("Vamos pedir os nomes e o peso")
time.sleep(1)
print("Vamos mostrar total pessoas cadastradas")
time.sleep(1)
print("Listagem pessoas mais pesadas")
time.sleep(1)
print("Pessoas mais leves")

lista = []


while True:
    lista.append([str(input("Nome: ")), int(input("peso: "))])
    escolha = str(input("Quer continuar? [S/N]"))
    if escolha == 'n':
        break

print(f"Total de pessoas cadastradas: {len(lista)}")

print() 

contador = 0
ordenado = sorted(lista, key=lambda x: x[1], reverse=True) 

#lambda x: x[1] pega o peso de cada item,
#key diz que é por esse valor que vai ordenar.
#x[0] → nome
#x[1] → peso

print(ordenado)

#tive de usar um for pra conseguir puxar os 3 maiores valores
print("Os maiores pesos são:")
for C in ordenado:
    print(f"O nome é {C[0]} e seu peso é {C[1]}") #Usei o C0 pro nome, e C1# pro peso
    contador += 1 
    if contador == 3:
        break

print()
ordenado_menor = sorted(lista, key=lambda x: x[1])
print()
print(ordenado_menor)
print("Os menores pesos são:")

contador = 0
for b in ordenado_menor:
    print(f"O nome é {b[0]} e seu peso é {b[1]}") #Usei o C0 pro nome, e C1# pro peso
    contador += 1 
    if contador == 3:
        break






