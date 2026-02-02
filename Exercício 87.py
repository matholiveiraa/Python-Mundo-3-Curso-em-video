#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para {[l]} e {[c]}: "))

print(matriz)
contador = 0

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}]", end="")
        for pularlinha in enumerate({matriz[l][c]}):
            contador+=1
            if contador % 3 == 0:
                print()

somatudo = (sum(matriz[0])) + (sum(matriz[1])) + (sum(matriz[2])) 
#A) Soma de todos digitados
print(f"A soma de todos os valores é: {somatudo}")

#B) Soma dos valores da terceira coluna
print(f"Soma valores terceira coluna: {sum(matriz[2])}")

#C)
print(f"O maior valor da segunda linha é: {max(matriz[1])}")
