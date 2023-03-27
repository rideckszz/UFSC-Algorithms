
def div (a):
    for i in range (1, a):
        if i % 3 == 0 or i % 7 == 0:
            print (i, end = " ")

n = int(input("Digite o numero: "))
resultado_final = div(n)  
print  (resultado_final)