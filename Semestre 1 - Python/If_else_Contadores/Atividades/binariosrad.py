numero = list(input("Digite o número bínario: "))
value = 0

for i in range(len(numero)):
	digit = numero.pop()
	if digit == '1':
		value = value + pow(2, i)

print("O valor decimal desse número é de: ", value)
