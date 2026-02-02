#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random


print("-"*40)
print("               MEGA CENA")
print("-"*40)

n = int(input("Quantos jogos você quer que eu sorteie?: "))
jogo = 0
while True:
    for N in range(n):
        jogo += 1
        lista = []
        for C in range(6):
            if C not in lista:
                lista.append(random.randint(1,60))
            
        print(f"jogo {jogo}:{lista}")
    break