#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
#crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        n % 2 != 0
        impar.append(n)
    escolha = str(input("Quer continuar? S/N: "))
    if escolha == "n":
        break

print(f"Sua lista: {lista}")
print(f"Sua lista pares: {par}")
print(f"Sua lista impares: {impar}")
    