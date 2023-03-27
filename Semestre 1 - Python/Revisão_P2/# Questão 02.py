# Questão 02
# Escreva uma função que dada uma lista de inteiros faça a média de todos os valores

lista = []
qndt_valores = int(input("Digite a quantidade de valores:  "))

def media (lista):
        soma = 0
        for item in range (len(lista)):
            soma = soma + lista [item]
            m = soma / qndt_valores
        return m 

for i in range (0, qndt_valores):
        numero = int(input("Digite a caceta do inteiro: "))
        lista.append(numero)

resultado = media(lista)

print (resultado)