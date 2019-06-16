
cont=0

dig = input("informe uma frase: ")
print("Ha '%i' espaços na frase.  "%(dig.count(" ")))

s = dig.count("a")+dig.count("e")+dig.count("i")+dig.count("o")+dig.count("u")
print("Ha '%i' vogais na frase.  "%(s))
