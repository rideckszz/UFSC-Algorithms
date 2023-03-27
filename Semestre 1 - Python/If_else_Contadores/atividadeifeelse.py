#Pedir inicio e fim ao usuario
#E digitar o n, informar se n pertence a esse intervalo

inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
n = int(input("Digite um numero: "))

if inicio > fim:
    aux = inicio
    inicio = fim
    fim = aux

if n >= inicio and n <= fim:
              print ("Seu número está dentro do intervalo")
    
else:
    print ("Seu número não está dentro do intervalo")
