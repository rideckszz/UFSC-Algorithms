#Somar listas

lista1 = [2, 4, 5, 9]
lista2 = [3, 5, 1, 3]
lista3 = []

for i in range (0, len(lista1)):
    soma = lista1 [i] + lista2 [i]
    lista3.append(soma)
    
print(lista3)
