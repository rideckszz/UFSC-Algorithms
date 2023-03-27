
                                                #Atividade 06

#  O usuário entrará com o número de linhas e com o número de colunas de uma matriz, ambos maiores que 0, e, em seguida, 
# com os valores da matriz, que serão números inteiros. O programa deve inicialmente imprimir a matriz inserida e depois 
# adicionar uma coluna a mais à matriz contendo a soma de cada linha e também uma linha adicional contendo a soma das colunas,
# e imprimi-la novamente. Segue abaixo um exemplo de execução do programa.

############################################# Parte da mat ####################################################

linhas_input = int(input("Digite o número de linhas: "))
colunas_input = int(input("Digite o número de colunas: "))
mat = []

for linha in range(0, linhas_input):
    mat.append([])
    for coluna in range(0, colunas_input):
        item = int(input("Digite o elemento: "))
        mat[linha].append(item)

print()

for linha in range(0, linhas_input):
    for coluna in range(0, colunas_input):
        print(mat[linha][coluna], end=" ")
    print()

print()

############################################# Parte da soma ####################################################

for r in range(0, linhas_input):
    mat[r].append(sum(mat[r]))
    print(*mat[r])

for coluna in range(0, colunas_input):
    somac = 0
    for linha in range(0, linhas_input):
        somac += mat[linha][coluna]
    print(somac, end=" ")




