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

entrada  = int(input("Digite a entrada: "))
lista_valores= [] 
qntd_dinheiro = []
total = 0 

#! Processamento:

if entrada == 4:
    qntd_notasde10 = int(input("Digite a quantidade de notas de 10: "))
    qntd_notasde20 = int(input("Digite a quantidade de notas de 20: "))
    qntd_notasde50 = int(input("Digite a quantidade de notas de 50: "))
    qntd_notasde100 = int(input("Digite a quantidade de notas de 100: "))
    qntd_dinheiro = [[100, qntd_notasde100], [50, qntd_notasde50], [20, qntd_notasde20], [10,qntd_notasde10]]
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


if entrada == 3:
    qntd_notasde10 = int(input("Digite a quantidade de notas de 10: "))
    qntd_notasde20 = int(input("Digite a quantidade de notas de 20: "))
    qntd_notasde50 = int(input("Digite a quantidade de notas de 50: "))
    qntd_dinheiro = [[50, qntd_notasde50], [20, qntd_notasde20], [10,qntd_notasde10]]
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

if entrada == 2:
    qntd_notasde10 = int(input("Digite a quantidade de notas de 10: "))
    qntd_notasde20 = int(input("Digite a quantidade de notas de 20: "))
    qntd_dinheiro = [[20, qntd_notasde20], [10,qntd_notasde10]]
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

if entrada == 1:
    qntd_notasde10 = int(input("Digite a quantidade de notas de 10: "))
    qntd_dinheiro = [[10,qntd_notasde10]]
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

lista_valores.reverse()
print (lista_valores)
