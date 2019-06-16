cont= 1
n=int(input("Digite um numero de 1 a 10"))
cont = 1
if n>=1 and n<=10:

 while cont<=10:
   tab = n * cont
   print (" %d X %d = %d ", n, cont, tab)
   cont = cont + 1
  
else:
  print ("apenas valores de 1 a 10")
