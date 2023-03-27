#Segundo tipo de resolução

a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))
c = float(input("Digite o terceiro numero: "))

if a < b:
    if b < c:
        print (a, b, c)
    else: #a < b >= c
        if a < c:
            print (a, c, b)
        else:
                print (c, a, b)
else: # a >= b ou b <= a
    if a < c:
        print (b, a, c)
    else: # b <= a >= c
        if b < c:
            print (b, c, a)
        else:
            print (c,b, a)
