teste = []

teste.append("Matheus")
teste.append(20)

galera = []

galera.append(teste[:])
teste[0] = 'Natalia'
teste[1] = 19

galera.append(teste[:])

print(galera)

galerinha = ['João', 19], ['Matheus', 20], ['Natalia',22], ['Ana', 18]
print(galerinha)

print(galerinha[2][0])

for P in galerinha:
    print(f'{P[0]} tem {P[1]} anos de idade.')