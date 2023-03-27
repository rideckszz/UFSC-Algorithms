# Verificar se é um triangulo
# a < b + c
# b < a + c
# c < a + b

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a < b + c and b < a + c  and c < a + b:
    if a == b and b == c:
        print ("Equilatero")
    elif a != b and b != c and c != a:
        print ("Escaleno")
    else:
        print ("Isosceles")
else: 
    print ("Não é triangulo")