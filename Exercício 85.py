#Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
import time
numeroslista = [[], []] #Uso de lista composta

print("Vamos pedir para você colocar número em uma lista")
time.sleep(1)
print("Você colocará os números e no final separaremos a lista entre par e impar, mas em ordem crescente")
time.sleep(1)
print("Vamos lá?!")

for C in range(7):
    n = int(input("\nDigite um número: "))
    if n % 2 == 0:
        numeroslista[0].append(n)
    else:
        n % 2 != 0
        numeroslista[1].append(n)
    
print(f"Números pares: {(sorted(numeroslista[0]))}")# Usei para mostrar a lista já em par

print(f"Números ímpares: {(sorted(numeroslista[1]))}")# Usei para mostrar a lista já em impar


