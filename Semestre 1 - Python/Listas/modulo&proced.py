#como se faz uma matriz?

matrizprincipal = []
linhamat = int(input("Digite o numero de linhas da matriz: "))
columat = int(input("Digite o número de colunas desejado : "))

for linha in range ( 0, linhamat):
    matrizprincipal.appent([])
    for coluna in range (0, columat):



#Função que classifique a idade escolar:

#def serie (idade):
 #   if idade > 0 and idade < 3:
  #      return ("berçário")
   # elif idade == 4 :
    #    return("pre 1")
   # elif idade == 5:
    #    return("pre 2")
   # else :
    #    return ("outros.")

#idade= int(input("Digite a idade da criança: "))
#s = serie(idade)
#print("a criaça será matriculada na série {}".format(serie))


#Aula do dia 12/07/2022

#def vezes (a,b):
 #   return a * b

#def antecessor (n):
    #return n-1 

def fatorial (m):
    f =1
    for i in range (1, m+1):
        f*= i
    return f

#POCEDIMENTO:

def tabuada(n):
    for i in range (1, 11):
        print(i * n, end + " ")
    print()

for i in range (1,10):
    tabuada(i)

#First exercise:função que retorne o maior entre dois valores:

def maiorvalor(n, m):
    if n > m:
        return n
    else:
        return m

###e se fosse pedido mais variaveis?

n = int(input("Digite o primeiro valor: "))
m = int(input("Digite o segundo valor: "))
o=int(input("Digite o segundo valor: "))
p=int(input("Digite o segundo valor: "))

#maior = maiorvalor(n,m)
r = maiorvalor(n,m)
r = maiorvalor (r, o)
r = maiorvalor (r, p)
print ("o maior é = ", maiorvalor)

#Função que conta a quantidade de números pares de uma matriz enviada como parâmetro