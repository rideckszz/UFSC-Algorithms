

idade = int(input("Digite uma idade: "))

if idade >= 1 and idade <= 4:
    print ("Berçario")
else:
    if idade == 5:
        print ("Pré 1")
    else:
        if idade == 6:
            print ("Pré 2")
        else:
            if idade == 7:
                print ("Primeira Série")
            else:
                if idade == 8:
                    print ("Segunda série")
                else:
                    print ("Não há matricula")