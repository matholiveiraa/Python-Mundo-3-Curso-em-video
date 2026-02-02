#Forma mais facil que aprendi a usar!
galera = []
totmenor = totmaior = 0

for C in range(0,3):
    galera.append([str(input("Nome: ")), int(input("Idade: "))])

print(galera)

#Forma do professor

galera1 = []
dado = []

for A in range(0,3):
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite a idade: ")))
    galera1.append(dado[:]) #aqui ele copiaria a lista e faria uma lista, depois repetiria e faria outra
    dado.clear() #inseri o dados na galeria mas logo apago os dados da lista dado, para quando adicionar n se repetir
print(galera1)

for p in galera1:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmaior += 1
    else:
        print(f'{p[1]} é menor de idade')
        totmenor += 1

print(f"Temos {totmaior} maiores e {totmenor} menores de idade")
