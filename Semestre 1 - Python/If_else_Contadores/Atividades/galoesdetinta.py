#Preço de tinta necessária para pintura
#Galões de 3,6 litros por 25 reais que cada litro cobre 18 metros quadrados

area = float(input("Digite a area que sera pintada: "))
galao = 18
valor = area // galao

if area % galao != 0:
    valor1 = valor + 1
    print (valor1)

else:
    print (valor)