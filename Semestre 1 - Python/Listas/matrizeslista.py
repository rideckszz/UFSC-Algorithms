

mat = [[0 , 2 , 4], [7, 9, 1], [3, 6, 9]]


for linha in mat:
    for item in linha:
        print(item, end = " ")
    print ()

print ()

for i in range (0, len(mat)):
    for j in range (0, len(mat[i])):
        print (mat[i][j], end = " ")
    print  ()


#montagem de matrizes vazias

#vazia = []

#matriz 2 x 3

#for linha in range (0, 2):
 #   vazia.append([])
  #  for i in range (0, 3):
   #     vazia[linha].append([])


#print (vazia)