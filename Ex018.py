import math
catOposto = float(input("Qual o comprimento do cateto oposto?"))
catAdjacente = float(input("Qual o comprimento do cateto adjacente?"))
hipotenusa = ((catOposto ** 2) + (catAdjacente ** 2)) ** 0.5
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))


catOposto = float(input("Qual o comprimento do cateto oposto?"))
catAdjacente = float(input("Qual o comprimento do cateto adjacente?"))
hipotenusa = math.hypot(catOposto, catAdjacente)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))