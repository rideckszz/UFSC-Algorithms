#Função que conta a quantidade de números pares de uma matriz enviada como parâmetro

mat = []

def imprimeMatriz (mat):
    for i in range (0, len(mat)):
        for j in range (0, len(mat[i])):
            print (mat[i][j], end = " ")
        print ()

def leiaMatriz(mat):
    nl = int(input("Digite linhas: "))
    nc = int(input("Digite Colunas: "))

    for i in range (0, nl):
        mat.append([])
        for j in range (0, nc):
            n = int(input("Digite valor: "))
            mat[i].append(n)

def contaPares(mat):
    cont = 0
    for i in range (0, len(mat)):
        for j in range (0, len(mat[i])):
            if (mat[i][j]) % 2 == 0:
                cont += 1
    
    return cont

m = []
leiaMatriz (m)
imprimeMatriz (m)
pares = contaPares (m)
print = ("Número de pares = ", pares)


