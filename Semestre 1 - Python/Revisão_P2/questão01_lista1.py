# Questão 01
# Escreva uma função que recebe 2 números float e retorna a soma, subtração, multiplicação e divisão desses números


def sum (a, b):
    return a + b

def sub (a, b):
    return a - b

def mult (a, b):
    return a * b

def div (a, b):
    return a / b

first_n = float(input("Digite um número: "))
second_n = float(input("Digite o número a receber a operação: "))

resultado_sum = sum (first_n, second_n)
resultado_sub = sub (first_n, second_n)
resultado_mult = mult (first_n, second_n)
resultado_div = div (first_n, second_n) 


print ("sum =", resultado_sum, "| sub =", resultado_sub, "| mult =", resultado_sub, "| div =", resultado_div)