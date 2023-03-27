#Armazenar 5 numeros em uma lista
#calcular a soma dos numeros da lista

lista = []

#Entrada

for i in range (0,5):
    n = int(input("Digite um elemento: "))
    lista.append(n)

#Calculo da soma (processo)
#sum(lista) = só do python, calcula todos os itens da lista

soma = 0

for item in lista:
    soma = soma + item
print (soma)

soma = 0
for i in range (0,len(lista)):
    soma = soma + lista[i]

lista = [i + [(sum(lista))] for i in lista]
#print (soma)
print(sum(lista))
print (lista)