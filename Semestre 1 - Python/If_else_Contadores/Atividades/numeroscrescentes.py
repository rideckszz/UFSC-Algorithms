#Entrar com três números e retornalos em ordem crescente (supondo que sao diferentes)

a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))
c = float(input("Digite o terceiro numero: "))

if a > b:
    aux = a
    a = b
    b = aux

if a > c:
    aux = a
    a = c
    c = aux

if b > c:
    aux = b
    b = c
    c = aux

print ("Ordem crescente: ", a, " ", b, " ", c)

#Para decrescente pode só substituir por c, b, a <<<<<
