x1 = int(input("Digite a primeira posicao: "))
y1 = int(input("Digite a segunda posição: "))
x2 = int(input("Digite onde que chegar: "))
y2 = int(input("Digite onde quer chegar 2: "))
z = abs(x1 - x2)
d = abs(y1 - y2)


if z + d == 3:
    print ("O cavalo consegue chegar nesta posição")
else:
        print ("O cavalo não consegue.")