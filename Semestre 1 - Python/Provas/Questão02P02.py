#Correção  prova questão 02

n = int(input("Digite o numero: "))

def sum (numero):
    soma = 0
    for i in range (0, numero + 1):
        soma += i
        print ("Seu numero atual é: ", i, " + ", soma - i )
        print ("Número atual: ", soma)
        

while n != 0 and n < 1001:
    sum (n)
    n = int(input("Digite o numero: "))
