#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = (
    "aprender", 
    "programar", 
    "linguagem", 
    "python", 
    "curso", 
    "gratis", 
    "estudar", 
    "praticar", 
    "trabalhar", 
    "mercado", 
    "programador", 
    "futuro")

for C in palavras: #Para cada C em palavras(lista)
    print (f"\nNa palavra {C} temos:", end="")
    for letra in C: #Para cada letra em C
        if letra.lower() in "aeiou":
            print(letra, end='')
