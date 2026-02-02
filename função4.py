def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2 # pega o valor da lista nessa posição e multiplica por 2
        posicao += 1                  # anda para a próxima posição  
    

listacomvalores = []


while True:
    
    inserir = int(input("Valor: "))
    listacomvalores.append(inserir)
    continuar = str(input("Continuar [S/N]: ")).lower()
    if  continuar == 'n':
        break

dobra(listacomvalores)
print(listacomvalores)

