#get an binary number input from  user
binario = int(input("Digite o numero que deseja converter:  "))
#create a decimal variable and set to 0
decimal=0
#initialize a variable i and set to 1
i = 1
#get the length of the binary number
tam = len(str(binario))
#logic to convert binary to decimal
sobra = binario
for k in range(tam):
    aux = binario % 10
    decimal = decimal + (aux * i)
    i = i * 2
    binario = int(binario/10)

if k > 1:
    print ("Não é binario")
else:
    print (" ", decimal)#display the decimal value

