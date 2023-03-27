# Questão 3
# Dada uma matriz 3x3 com uns e zeros verifique se cada linha está com os mesmos valores, se cada coluna está com os mesmos valores
# Como na tabela abaixo a primeira linha deve retornar True a segunda e terceira False igualmente para as colunas a 1 deve retornar 
# True e as outras duas False
# Você pode adicionar os resultados diretamente na matriz e imprimi-la, ou criar uma string que descreva cada condição satisfeita


mat = [[0, 1, 0], 
       [1, 1, 1], 
       [0, 1, 0]]

for i in range(0, len(mat)):
    valor = sum(mat[i])/len(mat[i])

    if  valor == 0 or valor == 1:
        mat[i].append(True)
        print(True)
    else:
        mat[i].append(False)
        print(False)
        
mat.append([])

for i in range(0, len(mat)-1):
    valor = (mat[0][i] + mat[1][i] + mat[2][i]) / (len(mat)-1)

    if  valor == 0 or valor == 1:
        mat[len(mat)-1].append(True)
        print(True)
    else:
        mat[len(mat)-1].append(False)
        print(False)
    
for item in mat:
    print(item)


