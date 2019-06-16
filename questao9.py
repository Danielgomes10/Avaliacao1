precomaca=1.8
precomorango=2.5
totalmaca= 0
totalmorango=0

pesomorango = float(input("Quantos kg de morango voce comprou?"))
pesomaca = float(input("Quantos kg de maca voce comprou?"))

if pesomorango > 5:
    totalmorango=(precomorango-0.3)* pesomorango
else:
    precomorango*pesomorango
    
if pesomaca > 5:
    totalmaca=(precomaca-0.3)* pesomaca
else:
    precomaca*pesomaca

if (totalmorango+totalmaca)>25 or (pesomorango+pesomaca)>8:
    final=(totalmorango+totalmaca)*0.9    

else:
   final=totalmorango+totalmaca

print("preco final da compra R$ ", final)
