#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for C in range(5):
    lista.append(int(input("Digite um número: ")))
print(f"O maior número foi {max(lista)}, sua casinha é a : {lista.index(max(lista))}")
print(f"O menor número foi {min(lista)}, sua casinha é a : {lista.index(min(lista))}")
