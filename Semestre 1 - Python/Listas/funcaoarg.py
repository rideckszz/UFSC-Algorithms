#Soma no python

def soma (*args):
    lista = list(args)
    print (lista)
    s = 0 
    for item in lista:
        s += item
    return s

def dobraLista(*args):
    lista = list(args)
    d = item
    for item in lista:
        d = item
        d = item * 2
    return d

r  = soma (2, 5, 10, 15)

print (r)
