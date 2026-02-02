#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média


pessoas = dict()
lista = list()
somaidades = 0


while True:
    pessoas.clear()

    pessoas['nome'] = str(input("Nome: "))

    while True:
        pessoas['sexo'] = str(input("Sexo [M/F]: ")).lower()

        if pessoas['sexo'] in 'mf':
            break


    pessoas['idade'] = int(input("Idade: "))
    somaidades += pessoas['idade']
    
    lista.append(pessoas.copy())
    while True:
        continuar = str(input("Quer continuar [S/N]: ")).lower()
        if continuar in 'sn':
            break
        print("Opção inválida! Tente novamente.")
    if continuar == 'n':
        break

print("-=" *30 )

print("-=" * 30)
print(f"Foram cadastradas {len(lista)} pessoas!")
print(f"A média das idade é {somaidades / (len(lista))}")
print("Mulheres: ")
for pessoas in (lista):
    if pessoas['sexo'] == 'f':
        print(f"{pessoas['nome']}")

print()

print("Pessoas maiores de idade: ")
for pessoas1 in (lista):
    if pessoas1['idade'] >= 18:
        print(f"{pessoas1['nome']}")



    


