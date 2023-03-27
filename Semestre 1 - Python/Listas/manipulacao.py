#Imprimir o dobro sem entrada

#Solicitar para o usuario uma lista de inteiros com 5 elementos e criar uma segunda lista em que cada 
#elemento é o dobro da anterior

#entrada
# a = [5, 7, 8, 10, 20]

#saida
#b = [10,14, 16, 20, 40]

lista1 = []
#lista2 = []
n = int(input("Digite a quantidade de elementos: "))

for i in range (0, n):
    e = int(input("Digite a lista: "))
    lista1.append(e)

#for item in lista1:
 #   lista2.append(item * 2)

#for i in range (0, len(lista1)):
 #   lista2.append(lista1[i] * 2)

lista2 = [ item * 2 for item in lista1 if item % 2 == 0]    #isso é do python

print (lista1)
print (lista2)