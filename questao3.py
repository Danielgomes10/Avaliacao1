altura = float(input("Digite sua altura"))
sexo = int(input("digite 1 se voce for homem e 2 se for mulher"))

if sexo == 1:
   pesoideal = ((72.7*altura)-(58))
else:
   pesoideal = ((62.1*altura)-(44.7))
   
print("Seu peso ideal e  ", pesoideal)
