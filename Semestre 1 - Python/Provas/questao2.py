#Questão 2

x = float(input("Digite o numero para fazer a operacao: "))
y = float(input("Digite o numero a ser operado: "))
oper = str(input("Digite a operacao a ser realizada: "))

if oper == "+":
    print ("Seu resultado é: ", (x + y))
else:
    if oper == "-":
        print ("Seu resultado é: ", (x - y))
    else:
        if oper == "*":
            print ("Seu resultado é: ", (x * y))
        else:
            if oper == "/" and y != 0:
                print ("Seu resultado é: ", (x / y))
            else:
                print ("Você não pode dividir por 0.")