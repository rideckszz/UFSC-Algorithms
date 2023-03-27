#Semana 5

#Obter o conceito (String) devido a um estudante em função da média de três notas (valores reais), o qual é obtido em função 
# da tabela

n1 = float(input("Digite sua primeira nota: ")) 
n2 = float(input("digite sua segunda nota:"))
n3 =  float(input("Digite sua terceira nota: "))
m = (n1 + n2 + n3) // 3

if m >= 0 and m < 6.0:
    print ("Insuf.")
else:
    if m >= 6.0 and m <= 7.5:
        print("Sati.")
    else:
        if m > 7.5 and m < 9:
            print ("Bom")
        else:
            if m >= 9 and m <=10:
                print ("Perfeito")
            else:
                print ("Sua nota quebra padrões")