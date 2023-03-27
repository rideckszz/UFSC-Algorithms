#Variáveis de input#
dia = int(input("Diga o dia: "))
mês = int(input("Diga o mês: "))
ano = int(input("Diga o ano: "))

#Doomsdays por ano#
if ano >= 1600 and ano < 1700 or ano >=2000 and ano < 2100:
    dd = 3
if ano >= 1700 and ano < 1800 or ano >=2100 and ano < 2200:
    dd = 1
if ano >= 1800 and ano < 1900 or ano >=2200 and ano < 2300:
    dd = 6
if ano >= 1900 and ano < 2000 or ano >=2300 and ano < 2400:
    dd = 4

#Fórmula pro Doomsday#
diffano = ano - (int(ano / 100)) * 100
leapyears = int(diffano/4)
mm7 = (int((leapyears + diffano + dd) / 7)) * 7
simpsem =(diffano + leapyears + dd - mm7)

#Ano bissexto#
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 !=0:
    bissexto = 1
else:
    bissexto = 0

#Meses igualdade#
if mês == 1:
    if bissexto == 1:
        doom = 4
    else:
        doom = 3
if mês == 2:
    if bissexto == 1:
        doom = 29
    else:
        doom = 28
if mês == 3:
    doom = 14
if mês == 5:
    doom = 9
if mês == 7:
    doom = 11
if mês == 9:
    doom = 5
if mês == 11:
    doom = 7
if mês != 2 and mês % 2 == 0:
    doom = mês

#Equação#
if dia > doom:
    resposta = abs(abs(dia - doom) - int((abs(dia - doom)) / 7) * 7 + simpsem)
if dia <= doom:
    resposta = abs(abs(dia - doom) - ((int(abs(dia - doom) / 7) + 1) * 7)) + simpsem

#resposta final#
if resposta == 0 or resposta == 7 or resposta == 14:
    print("é sábado")
if resposta == 1 or resposta == 8 or resposta == 15:
    print("é domingo")
if resposta == 2 or resposta == 9 or resposta == 16:
    print("é segunda")
if resposta == 3 or resposta == 10 or resposta == 17:
    print("é terça")
if resposta == 4 or resposta == 11 or resposta == 18:
    print("é quarta")
if resposta == 5 or resposta == 12 or resposta == 19:
    print("é quinta")
if resposta == 6 or resposta == 13 or resposta == 20:
    print("é sexta")