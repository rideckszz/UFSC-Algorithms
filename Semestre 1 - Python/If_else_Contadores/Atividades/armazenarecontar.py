#Armazenar 5 numeros em uma lista
#contar as ocorrencias de um determinado numero

lista = []

for i in range(0,5):
    x = int(input("Digite um numero: "))
    lista.append(x)

n = int(input("Digite o numero para pesquisar: "))

cont = 0

for item in lista:
    if item == n:
        cont = cont + 1

print (n, "apareceu", cont, "vezes.")