#Solicitar um numero para o usuario
#armazena a tabuada desse numero em uma lista

a = []
x = int(input("Digite o numero: "))

for i in range (0,11):
    tabu = x * i
    a.append(tabu)
    print (x, "x", i, "=", tabu)
print ()
print(a)