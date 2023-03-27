#informar se o numero é divisivel por 2,5 ou 10

numero = int(input("Digite o numero a ser dividido por 2, 5, 10: "))

if numero % 10 == 0:
    print ("É divisivel por 10, 5 e 2")
else:
    if numero % 5 == 0:
        print ("É divisivel por 5")
    else:
        if numero % 2 == 0:
            print ("É divisivel somente 2")
        else:
            print ("Não é divisivel por nenhum.")