#Solicitar dados de uma matriz nxm
#Solicitar tamanho da matriz
#Solicitar um numero e zerar a matriz nas posições em que o número ocorrer

mat = []
ordem = int(input("Digite a ordem: "))
linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))

for linha in range (0,ordem):
    mat.append([])
    for coluna in range (0,ordem):
        item = int(input("Digite o item: "))
        mat[linha].append(item)


for linha in range (0,ordem):
    for coluna in range (0,2):
        print (mat[linha][coluna], end = " ")
    print ()
