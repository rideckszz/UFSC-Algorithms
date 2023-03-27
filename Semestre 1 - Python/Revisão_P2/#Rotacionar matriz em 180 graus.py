#Rotacionar matriz em 180 graus



def reverseRow(data, index):
     
    cols = len(data[index])
    for i in range(cols // 2):
        temp = data[index][i]
        data[index][i] = data[index][cols - i - 1]
        data[index][cols - i - 1] = temp
     
    return data
 
def printMatrix(data):
     
    for i in range(len(data)):
        for j in range(len(data[0])):
            print(data[i][j], end = ' ')
         
        print()
 
def rotateMatrix(data):
     
    rows = len(data)
    cols = len(data[0])
     
    if (rows % 2):
        # Se N != 0 reverte a coluna do meio da matriz
        data = reverseRow(data, len(data) // 2)
        # trocar valor da matriz [i][j] por
        # [rows - i - 1][cols - j - 1] para obter metade das linhas
        for i in range(rows // 2):
            for j in range(cols):
                temp = data[i][j]
                data[i][j] = data[rows - i - 1][cols - j - 1]
                data[rows - i - 1][cols - j - 1] = temp
         
        return data
         
data = [ [ 1, 2, 3, 4, 5 ],
         [ 6, 7, 8, 9, 10 ],
         [ 11, 12, 13, 14, 15 ],
         [ 16, 17, 18, 19, 20 ],
         [ 21, 22, 23, 24, 25 ] ]
          
data = rotateMatrix(data)

printMatrix(data)