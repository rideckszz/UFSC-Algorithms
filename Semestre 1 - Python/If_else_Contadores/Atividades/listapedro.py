e = 0
decimal = 0
binario = 0

# Leia o número binário como inteiro.
numero = int(input("Digite um numero: "))
# Guarde aqui o resultado das divisões sucessivas.
sobra = numero
isBinary = 1

for i in list(str(numero)):
    if (i != "0") and (i != "1"):
        isBinary = 0

if (isBinary != 0):

# Faça os cálculos enquanto a divisão for maior que 0.
    while sobra > 0:
        aux = (sobra % 10) * (2 ** e)
        decimal = decimal + aux
        e = e + 1
        sobra = sobra // 10
    
    print (numero, "em decimal equivale a: ", decimal)
else:
    print (numero, "não é binario.")