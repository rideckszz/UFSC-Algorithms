
def mult (a):
    for i in range (1, a):
        if i % 3 == 0 or  i % 7 == 0:
            print (i, end = " ")
        else:
            pass

n = int(input("Digite o n: "))

resultado = mult(n)
