#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

campeonato = {}

for c in range(1):
    
    campeonato['nome'] = str(input("Nome do jogador: "))
    campeonato['quantidadepartidas'] = int(input("Digite quantos jogos ele jogou: "))
    campeonato['quantidadegols'] = 0
    campeonato['gols'] = []
    for quantidade in range(campeonato['quantidadepartidas']):
        n = int(input(f"Digite quantos gols fez na {quantidade+1}º partida: "))
        campeonato['gols'].append(n)
        campeonato['quantidadegols'] += n
print()

for keys,values in campeonato.items():
    print(f"{keys}: {values}")

print()
print(campeonato['gols'])
print(f"O jogador {campeonato['nome']} jogou {campeonato['quantidadepartidas']} partidas")

for a in range(campeonato['quantidadepartidas']):
    print(f"Na {a+1}º partida fez gols: {campeonato['gols'][a]}")