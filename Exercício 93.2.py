jogador = {}
partidas = []
jogador['nome'] = str(input("Nome do jogador: "))
total = int(input(f"Quantidade de partidas jogadas pelo {jogador['nome']}: "))

for c in range(0, total):
    partidas.append(int(input(f"Quantos gols fez na partida {c}: ")))

jogador['gols'] = partidas[:] #aqui ele faz exatamente uma copia
jogador['total'] = sum(partidas)

print("-=" *30)
print(jogador)
print("-=" *30)

print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas") #len para contar quantas partidas ele jogou, pela quantidade de gols

for indice, valor in enumerate(jogador['gols']):
    print(f"Na partida{indice+1} ele fez {valor} gols")