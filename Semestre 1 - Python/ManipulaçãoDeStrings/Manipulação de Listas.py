#Manipulação de Strings

#Trocar as strings

str1 = "A casa encantada quebou ontem"
str2 = str1.replace ("casa", "cama")

print (str1)
print (str2)

#Contar strings

#   Trocar um caracter na posição nao funciona:
        # str [0] = "b"

str1 = "A casa encantada quebou ontem"
str2 = str1.replace ("casa", "cama")

print (str1.count("ca"))

# x.capitalize() -> colocar letra em maiúsculo

str1 = "João"

print (str1.capitalize())  # = João

# isdigit() -> Verifica se a string é formada somente por digitos

numero = "12345"
letra = "1234a"

print (numero.isdigit())
print (letra.isdigit())

# Limpeza de strings:

str1 = ",, = .. python"
str2 = str1.strip("..==,, ")

print (str2)

#   Diferenciar itens

str1 = "Vaca não sabe nada, mas eu sou rei."
str2 = str1.split ()

print (str2)

#   Juntar/separar strs

txt = ("palava", "puta", "moranga", "vadia", "foda")
txt1 = (" e ")

txt_final = txt1.join(txt)

print (txt_final)