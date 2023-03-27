#Descobrir se um ano é bissexto

ano = int(input("Digie o ano que deseja saber se é bissexto: "))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print (ano, "é um ano bissexto!")
else:
    print (ano, "não é um ano bissexto.")
