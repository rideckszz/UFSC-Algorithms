#Verificar se estudante foi aprovado ou não

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = (nota1 + nota2 + nota3) // 3

if media >= 6.0:
    print("Sua média", media, "é suficiente e voce foi aprovado nesta matéria!")

else:
    print("Sua média", media, "não foi suficiente.")