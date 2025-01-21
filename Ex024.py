num = int(input("Digite um número positivo: "))

if num > 0:
    unidade = num // 1 % 10
    dezena = num // 10 % 10
    centena = num // 100 % 10
    milhar = num // 1000 % 10

    print("O número possui {} unidades, {} dezenas, {} centenas e {} milhares".format(unidade, dezena, centena, milhar))
    
else:
    print("Digite um número válido!")



