tamanho = int(input("Tamanho em metros quadrados: "))
litros = tamanho / 3

if tamanho % 54 == 0:
	latas = tamanho / 54
else: 
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ("latas",latas)
print (" preco total R$",preco)
