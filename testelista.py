num = [2,5,9,1]
num[2] = 3
print(num)


num.append(7) #Adicionando valor a lista
print(num)


num.sort() #Números em ordem
print(num)


num.sort(reverse=True) #Números ao contrário
print(num)


print(f"Essa lista tem {len(num)} elementos") #Contagem de elementos


num.insert(2, 0) #Na posição 2, inserir o 0
print(num)


num.pop() #Remove último valor da lista
num.pop(2) #Remove o elemento 2, não o número 2
print(num)



num.remove(7) #Remove número 7 da lista
print(num)

num.append(10)
num.append(8)
num.append(4)
num.append(1)
num.append(0)

num.sort()
print(num)

if 4 in num: #Usamos para remove numero 4 da lista
    num.remove(4)
else:
    print("Não achamos o 4")

print(num)
