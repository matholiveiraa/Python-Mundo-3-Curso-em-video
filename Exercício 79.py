#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

import time

print("Faremos um programa que você digitará dados, e na lista se tiver já algo igual ele não adiciona")

time.sleep(2)

print("Vamos lá!?")

time.sleep(2)

lista = []

while True:
    n = int(input("Digite um número: "))
    if n in (lista):
        print("Esse número já foi adicionado!")
    else:
        n not in lista
        lista.append(n)
        time.sleep(2)
    escolha = str(input("Você quer continuar? [S/N]: ")).lower()
    if escolha == "n":
        break
    time.sleep(1)
print(f"Valores da lista: {lista}")
    
