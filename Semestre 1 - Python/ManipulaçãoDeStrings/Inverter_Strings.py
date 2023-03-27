#                           Atividade em sala de aula 19/07
## Desenvolver uma função que recebe uma string e que devolve uma nova string invertida

def inverte(str1):
    str2 = ""
    for i in range (len(str1)-1, -1, -1):
        str2 += str1[i]
    if str2 == str1:
        return True
    else:
        return False

palavra = input("Digite a palavra: ")

print (inverte(palavra))



#           Forma que eu fiz:
#str = input("Digite a palavra que deseja inverter: ")
#inverso = " ".join(reversed(str))
#juntador = ""
#palavra_invertida = str.join(inverso)

#print (palavra_invertida)