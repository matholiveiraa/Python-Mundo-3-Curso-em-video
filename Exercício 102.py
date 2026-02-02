#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
#que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show = True):
    contador = 1
    for c in range(n, 0, -1):
        if show:
            print(f"{c} x ", end="")
            if c == 1:
                print("= ", end="")
        contador *= c
    return contador



n = int(input("Digite o número: "))
print(fatorial(n))
