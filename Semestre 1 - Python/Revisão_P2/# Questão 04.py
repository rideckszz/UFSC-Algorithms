# Questão 04
# Dada a seguinte lista = [[“Andre”, 1500], [“Carlos”, 400], [“Jose”, 4000]], crie uma função que recebe a lista e a porcentagem
#  geral para calcular o aumento de salário de cada um, e me retorne a lista e coloque na lista do emprego um indicativo de True
#  caso o salário passa dos 2000 com o aumento.


lista = [["Andre", 1500], ["Carlos", 400], ["Jose", 4000]]
aumento = float(input("Digite o aumento: "))

def calcula_aumento_salario(lista, porcentagem):
    for funcionario in lista:
        funcionario.append(funcionario[1])
        funcionario[1] += (funcionario[1]/100) * porcentagem
        if funcionario[1] > 2000:
            funcionario.append(True)
        else:
            funcionario.append(False)
        
    return lista

resultado = calcula_aumento_salario(lista,aumento)

print(resultado)