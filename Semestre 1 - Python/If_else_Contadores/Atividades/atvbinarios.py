#Atividade 04 - Convertor de números bínarios

# Leia o número binário como inteiro.
binario = int(input("Digite o número bínario: "))

# Este é o contador que representa o expoente.
decimal = 0

# Crie outras variáveis que for utilizar.
i = 1
aux2 = binario
aux = binario % 10
# Faça os cálculos enquanto a divisão for maior que 0.
# Para um número como 1011, a ideia é ir dividindo,
# de forma que se obtenha 1011, depois 101, depois 10 e assim por diante.
while binario > 0:
  aux = binario % 10
   # Obtenha o dígito mais à direita utilizando a operação de resto.
  decimal = decimal + (aux * i)
  # Atualize as variáveis sobra e expoente.
  i = i * 2
  binario = int(binario / 10)
  if aux > 1:
    print ("Não é binario")
  else:
    if aux <= 1:  
      print (aux2, "em decimal é", decimal)
    else:
      print(aux2, "não é um dígito binário")
