#Crie um programa que simule um temporizador. O usuário entrará com a quantidade de minutos e de segundos,
# respectivamente



min = int(input("Digite a quantidade de minutos: "))
sec = int(input("Digite a quantidade de segundos: "))
tempo = min * 60 + sec

while tempo:
    #minutes, second = divmod(tempo, 60) 
    minutes = tempo // 60
    seconds = tempo % 60
    print(minutes, "minutos e", seconds, "segundos")
    tempo = tempo - 1

print ("O tempo acabou!")
