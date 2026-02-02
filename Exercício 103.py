#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome_jogador="<desconhecido>", quantidade_gols_jogador=0):
    
    print(f"{nome_jogador}, fez isso de gols!: {quantidade_gols_jogador}")




nome_jogador = input("Nome do jogador: ")
if nome_jogador.isnumeric():
    nome_jogador = "<desconhecido>"
else:
    nome_jogador == ""
    nome_jogador = "<desconhecido>"

quantidade_gols_jogador = input("Quantidade de gols do jogador: ")
if quantidade_gols_jogador.isnumeric():
    quantidade_gols_jogador = quantidade_gols_jogador
else:
    quantidade_gols_jogador != int
    quantidade_gols_jogador = 0


ficha(nome_jogador, quantidade_gols_jogador)