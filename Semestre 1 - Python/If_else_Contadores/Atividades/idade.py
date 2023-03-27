idade1 = int(input("Digite a idade da pessoa 1: "))
peso1 = float(input("Digite peso da pessoa 1: "))
nome1 = str(input("Digite so nome da segunda pessoa: "))

idade2 = int(input("Digite a idade da pessoa 2: "))
peso2 = float(input("Digite peso pessoa 2: "))
nome2 = str(input("Digite o nome da segunda pessoa: "))

idade3 = int(input("Digite a idade da pessoa 3: "))
peso3 = float(input("Digite peso pessoa 3: "))
nome3 = str(input("Digite o nome da terceira pessoa: "))

if idade1 > idade2:
    maioridade = idade1
    maiorpeso = peso1
    maiornome = peso1

else:
    maioridade = idade2
    maiorpeso = peso2
    maiornome = nome2

if maioridade < idade3:
    maioridade = idade3
    maiorpeso = peso3
    maiornome = nome3

print (maiornome, "é a pessoa mais velha com", maioridade, "e pesa", maiorpeso)
