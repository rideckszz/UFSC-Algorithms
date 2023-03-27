# Salario INSS

#Calcular o valor da seguridade social INSS do funcionário de uma empresa, sabendo que ele é calculado segundo a tabela que segue, 
# aplicada ao salário bruto deste funcionário:

#   salário bruto até R$ 720,00 tem um valor de 7.65% sobre o salário bruto;
#   salário bruto até R$ 1.200,00 tem um valor de 9% sobre o salário bruto;
#   salário bruto até R$ 2.400,00 tem um valor de 11% sobre o salário bruto;
#   salário bruto acima de R$ 2.400,00 tem um valor de 11% sobre R$ 2.400,00;

salario = float(input("Digite seu salário bruto: "))
salario720 = salario * 0.765
salario1200 = salario * 0.9
salario2400 = salario * 1.1
salariomaior = salario + salario2400

if salario <= 720:
    print (salario720)
else:
    if salario <= 1200:
        print (salario1200)
    else:
        if salario <= 2400:
            print (salario2400)
        else:
            print (salariomaior)