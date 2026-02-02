#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                               
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []


while True:
    n = int(input("Digite um número: "))
    escolha = str(input("Quer continuar? [S/N]: ")).lower()
    lista.append(n)
    if escolha == "n":
        break
print(f"Foram digitado {len(lista)} valores")


if 5 in lista:
    print(f"Foi digitado o valor 5 na lista, o 5 está na casinha: {lista.index(5)+1}")
print("Bye Bye")

nova = sorted(lista, reverse=True)
print(f"Ordem decrescente: {nova}")
    
