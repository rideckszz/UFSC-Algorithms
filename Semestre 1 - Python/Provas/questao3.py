#Questão 3

minutos = int(input("Digite a quantidade de minutos: "))

if minutos < 200 and minutos > 0:
    plano1 = minutos * 0.20
    print ("Seu plano é de : ", plano1)
else:
    if minutos >= 200 and minutos <= 400:
        plano2 = minutos * 0.18
        print("Seu plano é de : ", plano2)
    else:
        if minutos > 400:
            plano3 = minutos * 0.18
            print ("Seu plano é de : ", plano3)

