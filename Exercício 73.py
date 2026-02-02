#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.

timesfutebol = (
    "Athletico Paranaense",
    "Atlético-MG",
    "Bahia",
    "Botafogo",
    "Chapecoense",
    "Corinthians",
    "Coritiba",
    "Cruzeiro",
    "Flamengo",
    "Fluminense",
    "Grêmio",
    "Internacional",
    "Mirassol",
    "Palmeiras",
    "Red Bull Bragantino",
    "Remo",
    "Santos",
    "São Paulo",
    "Vasco da Gama",
    "Vitória")

print(timesfutebol[:5]) #correto
print(timesfutebol [-4:]) #correto
print(sorted(timesfutebol)) #correto, já estava em ordem alfabética
print(f"O Chapecoense está na posição: {timesfutebol.index("Chapecoense")+1}")

