# Questão 05
# Cire uma funçao 

lista = ["Joel", "Puta", "Filósofa"]
string = str(input("Digite a palavra: "))

def verifica (lista,string):
    for i in range(len(lista)):
        print(lista[i])
        if string == lista[i]: 
            return True
        else:
            pass

    return False     

resultado = verifica (lista, string)

print (resultado)
        

