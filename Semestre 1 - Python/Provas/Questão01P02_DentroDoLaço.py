#Correção  prova questão 01

lista_A = [3, 5, 10, 8, 7]
lista_B = [4, 2, 5, 9, 6]

def mult (lista_1, lista_2):
    lista_C = []
    for i in range (0, len(lista_1)):
        resul = lista_1[i] * lista_2 [i]
        lista_C.append(resul)
    return lista_C
    
resultado_final = mult(lista_A, lista_B)  

print (resultado_final)
