mat = []

for linha in range (0,3):
    mat.append([])
    for coluna in range (0,2):
        item = int(input("Digite o item: "))
        mat[linha].append(item)

soma = 0

for linha in mat:
    for item in linha:
        soma += item 
print ("A soma é de: ", soma)

somacoluna = 0 

for coluna in range (0,2):
    somacoluna += mat[0][coluna]
print ("A soma de colunas é: ", somacoluna)

somalinha = 0 
for linha in range (0,3):
    somalinha += mat[linha][0]
print ("Soma das linhas é: ", somalinha)

for linha in range (0,3):
    for coluna in range (0,2):
        print (mat[linha][coluna], end = " ")
    print ()