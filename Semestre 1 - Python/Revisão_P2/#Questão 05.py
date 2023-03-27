#Questão 05

lista_final = []
qPessoas = int(input("Digite a quantidade de pessoas: "))

def cadastro (lista):
    nome = str(input("Digite o nome da pessoa: "))
    ano = int(input("Digite a data de nascimento da pessoa: "))
    cargo = str(input("Digite o cargo: "))
    idade = 2022 - ano
    lista.append([nome, ano, cargo, idade])
    return lista

for i in range(qPessoas):
    lista_final = cadastro(lista_final)
    
for i in range(qPessoas):
    print(lista_final[i])
