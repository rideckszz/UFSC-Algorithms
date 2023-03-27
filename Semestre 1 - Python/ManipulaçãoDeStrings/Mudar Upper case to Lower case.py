#       Atividade Strings 19/07
#
## Trocar todas as letras minusculas por maiusculas


#palavra = str(input("Dgite a palavra: "))

#          Metódos do python:

#str0 = palavra.upper()
#print (str0)
#print (str0.lower())

####################################################3

def upper_case_letter (letra):
    if letra >= "a" and letra <= "z":
        n = ord(letra) - 32
        letra = chr(n)
        return letra
    return letra

def upper_case_word (palavra):
    str0 = ""
    for i in palavra:
        str0 += upper_case_letter(i)
    return str0

def lower_case_letter (letra):
    if letra >= "A" and letra <= "Z":
        n = ord(letra) + 32
        letra = chr(n)
        return letra
    return letra

def lower_case_word (palavra):
    str1 = ""
    for i in palavra:
        str1 += lower_case_letter(i)
    return str1

palavra_input = input("Digite a palavra: ")

print (upper_case_word(palavra_input))
print (lower_case_word(palavra_input))