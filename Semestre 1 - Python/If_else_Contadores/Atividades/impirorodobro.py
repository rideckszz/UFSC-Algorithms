#Solicitar para o usuario uma lista de inteiros com 5 elementos e criar uma segunda lista em que cada 
#elemento é o dobro da anterior

#entrada
# a = [5, 7, 8, 10, 20]

#saida
#b = [10,14, 16, 20, 40]

lista1 = []
lista2 = []
n = int(input("Digite a quantidade de elementos: "))

for i in range (1, n):
    e = int(input("Digite a lista: "))
    lista1.append(e)
    lista2.append(e * 2)

print (lista1)
print (lista2)


