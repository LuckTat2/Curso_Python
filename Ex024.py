num = int(input("Digite um número positivo: "))

if num > 0:
    unidade = num % 10
    dezena = num % 100 // 10
    centena = num % 1000 // 100
    milhar = num % 10000 // 1000

    print("O número possui {} unidades, {} dezenas, {} centenas e {} milhares".format(unidade, dezena, centena, milhar))
    
else:
    print("Digite um número válido!")



