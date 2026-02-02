#.count()
#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


import time

print("Iremos montar um programa que leia uma expressão e diga se ela está correta!")

time.sleep(2)

print("Vamos lá?")

time.sleep(2)

expressao = str(input("Digite sua expressão: "))

abertas = expressao.count('(')
fechadas = expressao.count(')')

print(abertas)
print(fechadas)

if abertas == fechadas:
    print("A expressão está correta")
else:
    print("A expressão está errada")