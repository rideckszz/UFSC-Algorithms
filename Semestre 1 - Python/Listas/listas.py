#Solicitar 5 numeros para o usuario e armazenar os mesmos em uma lista, depois imprimilos

a = []
x = int(input("Digite o numero de algarismos: "))

for i in range (0,x):
    y = int(input("Digite o numero: "))
    a.append(y)

for item in a:
    print (item, end= " ")

print()
print(a)