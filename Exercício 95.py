#Aprimore o desafio 93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas quantidadepartidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
import copy

time = list()
jogador = dict() #Utilizado para aceitar dados e apagar em seguida
quantidadepartidas = list() #Utilizado apenas para contagem de aprtidade

while True:
    quantidadepartidas.clear()
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    total = int(input(f"Quantidade de jogadas pelo {jogador['nome']}: "))

    for contador in range(0, total):
        quantidadepartidas.append(int(input(f"Quantos gols fez na partida {contador}: ")))

    jogador['gols cada partida'] = quantidadepartidas[:] #aqui ele faz exatamente uma copia da quantidade de partidas
    jogador['total'] = sum(quantidadepartidas) #logo apos tem o total que seria o pelo total de gols

    
    time.append(jogador.copy()) #Inserir o dados jogados no time.
    
    

    while True:
        continuar = str(input("Quer continuar [S/N]: ")).lower()
        if continuar in 'sn':
            break
        print("Opção inválida! Tente novamente.")
    if continuar == 'n':
        break

for keys,values in enumerate(time):
    print(f"{values}")
    

