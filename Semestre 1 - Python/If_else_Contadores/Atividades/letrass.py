
letra = input("Digite a letra: ")

tam = ord(letra)


if ord(letra) in range (65, 90) and ord(letra) in range (141,172):
    print (tam, "é uma letra")

else:
    print(tam, "não é uma letra")