#Atividade Saltador

# No último campeonato mundial de atletismo foram anotados as marcas dos 3 saltos em distância de cada um dos atletas, 
# juntamente com o seu nome. Imprima o nome do primeiro colocado entre 4 atletas, sendo que o primeiro colocado é aquele que 
# obteve o maior salto.

#Nota mental: ver atividade do número crescente
#lembrar de todas as variáveis

a = str(input("Digite o nome do atleta 1: "))
asalto1 = float(input("Digite o valor do salto 1: "))
asalto2 = float(input("Digite o valor do salto 2: "))
asalto3 = float(input("Digite o valor do salto 3: "))

if asalto1 > asalto2 and asalto1 > asalto3:
    maiorA = asalto1
else:
    if asalto2 > asalto3:
        maiorA = asalto2
    else :
        maiorA = asalto3

b = str(input("Digite o nome do atleta 2: "))
bsalto1 = float(input("Digite o valor do salto 1: "))
bsalto2 = float(input("Digite o valor do salto 2: "))
bsalto3 = float(input("Digite o valor do salto 3: "))

if bsalto1 > bsalto2 and bsalto1 > bsalto3:
    maiorB = bsalto1
else:
    if bsalto2 > bsalto3:
        maiorB = bsalto2
    else:
        maiorB = bsalto3

c = str(input ("Digite o nome do atleta 3: "))
csalto1 = float(input("Digite o valor do salto 1: "))
csalto2 = float(input("Digite o valor do salto 2: "))
csalto3 = float(input("Digite o valor do salto 3: "))

if csalto1 > csalto2 and csalto1 > csalto3:
    maiorC = csalto1
else:
    if csalto2 > csalto3:
        maiorC = csalto2
    else:
        maiorC = csalto3

d = str(input("Digite o nome do atleta 4: "))
dsalto1 = float(input("Digite o valor do salto 1: "))
dsalto2 = float(input("Digite o valor do salto 2: "))
dsalto3 = float(input("Digite o valor do salto 3: "))

if dsalto1 > dsalto2 and dsalto1 > dsalto3:
    maiorD = dsalto1
else:
    if dsalto2 > dsalto3:
        maiorD = dsalto2
    else :
        maiorD = dsalto3

if maiorA == maiorB:
    print ("Houve um empate entre ", a, " e ", b,)
else:
    if maiorA == maiorC:
        print ("Houve um empate entre ", a, " e ", c)
    else:
        if maiorA == maiorD:
            print ("Houve um emapte entre ", a, " e ", d)
        else:
            if maiorB == maiorC:
                print ("Houve um emapte entre ", b, " e ", c) 
            else:
                print ("Houve uma empate.")

if maiorA > maiorB and maiorA > maiorC and maiorA > maiorD:
    print ("O atleta com o maior salto foi ", a)
else:
    if maiorB > maiorC and maiorB > maiorD:
        print ("O atleta com o maior salto foi ", b)
    else:
        if maiorC > maiorD:
            print("O atleta com o maior salto foi ", c)
        else: 
            print("O atleta com o maior salto foi ", d)
