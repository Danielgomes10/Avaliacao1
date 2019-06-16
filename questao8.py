cont = 0
resp = str(input("Telefonou para a vítima?"))

if resp == "sim" :cont=cont+1 

resp = str(input("Esteve no local do crime?"))
if resp == "sim" :cont = cont + 1 

resp = str(input("Mora perto da vítima?"))
 
if resp == "sim" :cont = cont + 1 
resp = str(input("Devia para a vítima"))

if resp == "sim":cont = cont + 1

resp = str(input("Já trabalhou com a vítima?"))

if resp == "sim":cont = cont + 1 
if cont == 2:print("Suspeita")
if cont == 3 or cont == 4:print("Cúmplice")
if cont == 5:print("Assassino")
else:print("Inocente")
