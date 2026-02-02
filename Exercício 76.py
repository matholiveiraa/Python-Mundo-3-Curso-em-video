#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
#na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#Inserção de dados na tupla listagem
Listagem = (
    
            "Lapis", 0,75,
            "Borracha", 1.30,
            "Mochila", 85.00,
            "Caneta", 2.00,
            "Corretivo", 4.50)

#Zona de formatação de texto e título
print("-" *40)
print(f"{"LISTAGEM DE PREÇO":^40}")
print("-" *40)

for C in range(0, len(Listagem)): #Usei len para ir até o final
    if C % 2 != 0:
        print(f"{Listagem[C]:.<30}" , end ="")
    else:
        print(f"R${Listagem[C]}")





