
lista = [2, 50, 10, 15, 30]

#a = lista[2:5]

#Cortando a lista da posição 2 até a 5 (4)
for i, item in enumerate (lista[2:5]): #(a)
    print (i, item)

lista.reverse()

for item in lista:
    print(item, end = " ")

#codigo longo para reverter

tam = len(lista)

for i in range(0, tam//2):
    aux = lista[i]
    lista[i] = lista [tam - 1 - i]
    lista [tam - 1 - i] = aux
for item in lista:
    print(item, end = " ")

#ordenar lista crescente
lista.sort()
print()
for item in lista:
    print (item, end = " ")