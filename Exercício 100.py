#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
import random


def sorteia(lista_numeros):
    contador = 0
    
    for sorte in range(5):
        contador += 1
        sorte = random.choice(lista_numeros)
        if sorte % 2 == 0:
            outra_lista.append(sorte)
        print(f"{contador}º sorteado = {sorte}")

def somapar(outra_lista):
    total = sum(outra_lista)

    print(f"A soma total dos pares é: {total}")

#listas
lista_numeros = [10,8,4,2,3,6,8,44,4,6,64,35,345,534,1]
outra_lista = []

#Usa função
sorteia(lista_numeros)
print(f"Números pares: {outra_lista}")
somapar(outra_lista)

