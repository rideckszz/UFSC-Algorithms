#Receber 10 valores e mante_los caso sejam  < que o atual na lista

d = [2, 4, 6, 4, 10, 15, 30, 3, 5, 19]
n = int(input("Digite a quantidade de elementos: "))
maior = d[0]

for i in range (0, n):
    e = int(input("Digite o elemento: "))
    d.append(e)

cont = 0
#maior = d[0]

for i in range (0, len(d)):
    # if d[i] > maior:
    if d[i] > d[cont]:
        #maior = d[i]
        cont = i

print (maior)
print (cont)

#print(max(d))
#print(min(d))