#Atividade 4 - Binario para decimal

#Variaveis
e = 0
decimal = 0
binario = 0

# Leia o número binário como inteiro.
numero = int(input("Digite um numero: "))
# Guarde aqui o resultado das divisões sucessivas.
sobra = numero

# Faça os cálculos enquanto a divisão for maior que 0.
while sobra > 0:
    # Obtenha o dígito mais à direita utilizando a operação de resto.
    binario = sobra % 10
    if binario > 1:
        # Caso o dígito não seja binário...
        break
    # Calcule aqui a contribuição do dígito para o número decimal.
    aux = binario * (2 ** e)
    decimal = decimal + aux
    e = e + 1
    sobra = sobra // 10

if binario > 1:
    print (binario, "não é binario.")
else:
    print (numero, " em decimal equivale a: ", decimal)
