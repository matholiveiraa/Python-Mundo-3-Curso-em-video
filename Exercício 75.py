import time
#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.

numeros = (
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: "))
)

print(numeros)
print(f"Valor 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"Valor 3 foi digitado pela primeira vez na: {numeros.index(3)+1} vez")
else:
    print("Número 3 não está na tupla")
    
for par in numeros: #Para expressar números pares
    if par % 2 == 0:
        print(par)

