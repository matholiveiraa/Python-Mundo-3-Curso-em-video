valores = []
valores.append(5)
valores.append(9)
valores.append(4)



for c, v in enumerate(valores):
    print(f"\bNa posição {c}, encontrei o valor {v}")
print("Chegamos ao final da lista")

for mais in range(5):
    valores.append(int(input("Digite um valor para a lista: ")))
print(f"Esses são os valores da lista: {valores}")

valores2 = list()
for cont in range(0,5):
    valores2.append(int(input("Digite um valor")))

for a, b in enumerate(valores2):
    print(f"\bNa posição {a}, encontrei o valor {b}")
print("Chegamos ao final da lista")

