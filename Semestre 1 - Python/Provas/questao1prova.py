#Questão 1

cont = 0
n = float(input("Digite o primeiro numero a ser somado: ")) 
soma = n

while n != 0:
    cont = cont + 1
    n = float(input("Digite o numero a ser somado: "))
    soma = soma + n
    print("Soma atual de: ", soma)
    media = soma / cont
print ("A soma total dos numeros foi: ", soma, ", o total de numeros contados foi de: ", cont, "e a media dos numeros foi de: ", media)