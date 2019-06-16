valorhora = float(input("quanto voce ganha por hora?"))
horames = float(input("quantas horas voce trabaha por mes?"))

salariobruto = (valorhora * horames)
ir = (salariobruto * 0.11)
inss = (salariobruto * 0.08)
sindicato = (salariobruto * 0.05)
liquido = (salariobruto - ir)-(inss - sindicato)

print (" Salário Bruto : R$", salariobruto)
print (" IR: R$",ir )
print ("INSS: R$" ,inss )
print ("Sindicato: R$", sindicato )
print (" Salário Liquido : R$",liquido)
