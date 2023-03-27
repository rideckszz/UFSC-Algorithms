#                              Atividade Online 6 - 7 (A06 e A07): Saque de valor em Caixa Eletrônico
#   Num caixa eletrônico estão disponíveis uma certa quantidade de cédulas de diferentes valores e em ordem crescente de valor, 
# conforme exemplificado abaixo. Quando um cliente realiza um saque, é necessário determinar quantas cédulas de cada tipo serão
# necessárias para efetuar o saque. Por exemplo, suponha que num caixa eletrônico tenhamos notas conforme a tabela.
#   Considerando que o critério para cálculo é o de oferecer ao cliente o menor número possível de notas, a título de exemplo considere
# que um cliente deseja realizar saque de  R$ 360,00. Neste caso são necessárias 3 notas de R$ 100,00, 1 nota de R$ 50,00 e 1 cédula
# de R$ 10,00.

# Todo: 
#*  Criar matriz com valores
#*  Lista para qnt. de dinheiro
#*  Percorrer ambas
#*  Fazer com que diga quanbdo não existe tal valor

#!Var's:

lista_valores= [] 
qntd_dinheiro = [[100, 10], [50, 20], [20, 20], [10, 50]]
total = 0 

#! Processamento:

for nota in qntd_dinheiro: 
    total += nota[0] * nota[1] 
saque = int(input("Informe o valor a ser sacado: ")) 

if saque > total: 
    print("Este valor não está disponível para saque.")

else:
    for nota in qntd_dinheiro: 
        qntd_notas= saque // nota[0] 
        saque -= qntd_notas * nota[0] 
        nota[1] -= qntd_notas
        lista_valores.append(qntd_notas) 

#! Print's

print (lista_valores)