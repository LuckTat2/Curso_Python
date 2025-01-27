nome = str(input("Digite seu nome: "))
if nome == "Lucas":
    print("Que nome lindo!")
else:
    print("Seu nome é tão normal!")
print("Bom dia, {}!".format(nome))


n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
m = (n1+n2)/2
print("A sua média foi {:.1f}".format(m))
#print("Parabéns!" if m>=6.0 else ("Estude mais!"))
if m >= 6.0:
    print("Sua média foi boa! Parabéns!")
else:
    print("Sua média está ruim! Estude mais!")



