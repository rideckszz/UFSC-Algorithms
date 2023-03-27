# Custo de locação de um veículo (moodle)
d = int(input("Digite quantos dias vc locou o carro: "))
km = int(input("Digite quantos km vc andou com o carro: "))
preco = (45 * d) 

if km > 60:
    print (preco + 0.50 * km - 60)
else:
    print (preco)