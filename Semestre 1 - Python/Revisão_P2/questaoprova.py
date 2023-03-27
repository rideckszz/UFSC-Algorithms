n = int(input("h"))
soma = 0

def mult (a):
    for i in range (0, a - 1):
        soma = 0
        soma = soma + i
        aux = soma
        print (soma)
    return soma 

while n != 0:
    n = int(input("Digite o numero a ser somatoriado: "))
    mult (n)