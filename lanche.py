lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")
#Tupla: são imutáveis
print(lanche[-2])
print(lanche[1:4])
print(lanche[2:])
print(lanche[:2])

for pos, c in enumerate(lanche):
    print(f"Eu vou comer {c}, na posição {pos}")
    
print(lanche)
print(sorted(lanche)) #Ordem alfabética

a = (2,5,4)
b = (5,8,1,2)
m = a + b #cola as duas tuplas
print(m)
print(m.count(5)) #quantas vezes aparece numero 5 
print(m.index(8)) #Qual posição está o 8
del(m)
print(m)
