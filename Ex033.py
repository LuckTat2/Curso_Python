distancia = float(input("Qual é a distância da sua viagem?"))

print("Você está prester a começar uma viagem de {:.1f}Km.".format(distancia))

'''if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45'''

passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("E o preço da sua passagem será de R${:.2f}".format(passagem))