#Solicitar 3 valoras e informar o maior (a,b,c)

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a > b and a > c:
    print ("A é maior que b e c")

if b > a and b > c:
    print ("B é maior que c e a")

if c > a and c > b:
    print ("C é maior que b e a")

###############################################################################################

#if a > b:
 #   maior = a
#else: 
  #  maior = b

#if maior < c:
   # maior = c

#print (maior)