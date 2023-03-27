
mat = []

coluna1 = int(input("Digite a posição da primeira coluna: "))
coluna2 = int(input("Digite a posição da segunda coluna: "))
ordem = int(input("Digite a ordem: "))


for linha in range(0, ordem):
    aux = mat[linha][coluna1]
    mat[linha][coluna1] = mat[linha][coluna2]
    mat[linha][coluna2] = aux
print ()


for linha in range (0,ordem):
    for coluna in range (0,ordem):
        print (mat[linha][coluna], end = " ")
    print ()
