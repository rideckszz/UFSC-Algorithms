#Somar listas em python


############################################# Parte da matriz #######################################################################
mat = []
linha_input = int(input("Digite o número de linhas da matriz: "))
colunas_input = int(input("Digite o número de colunsa da matriz: "))

for linha_mat in range (0, linha_input):
    linha = []
    mat.append(linha)
    for coluna_mat in range (0, colunas_input):
        integer = int(input("Digite o inteiro na matriz: "))
        mat[linha_mat].append(integer)

for linha_mat in range (0, linha_input):
    for coluna_mat in range (0, colunas_input):
        print (mat[linha_mat][coluna_mat], end = " ")
    print ()

################################################ Parte da soma ######################################################################

soma = 0
lista_aux = 0

for linha_mat in mat:
    for item in linha_mat:
        soma += item 
print ("A soma é de: ", soma)

somalinha = 0 
for linha_mat in range (0, linha_input):
    somalinha += mat[linha_mat]
print ("Soma das linhas é: ", somalinha)



