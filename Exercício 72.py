import time

print("Iremos fazer um programa que você tem que escolher de 0 a 20")

time.sleep(2)

lista = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
    "Seis", "Sete", "Oito", "Nove", "Dez",
    "Onze", "Doze", "Treze", "Catorze", "Quinze",
    "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
)

print(len(lista))

while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if 0 <= n <= 20:
        break
print(f"Você digitou: {lista[n]}")

        
    
