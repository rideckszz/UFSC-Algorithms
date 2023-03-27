# Leia o número binário como inteiro.
binario = int(input("Digite o número que deseja transformar: "))

# Guarde aqui o resultado das divisões sucessivas.
sobra = binario
 
# Este é o contador que representa o expoente.
# Pesquise sobre a conversão com notação posicional.
expoente = 0
 
# Crie outras variáveis que for utilizar.
# 
 
# Faça os cálculos enquanto a divisão for maior que 0.
# Para um número como 1011, a ideia é ir dividindo,
# de forma que se obtenha 1011, depois 101, depois 10 e assim por diante.
while sobra > 0:
  # Obtenha o dígito mais à direita utilizando a operação de resto.
  digito = binario % 10
  if digito > 1:
    # Caso o dígito não seja binário...

  # Calcule aqui a contribuição do dígito para o número decimal.
  decimal += digito 
 
  # Atualize as variáveis sobra e expoente.
  # ...
 
if digito <= 1:
  print(binario, "em decimal é", decimal)
else:
  print(digito, "não é um dígito binário")