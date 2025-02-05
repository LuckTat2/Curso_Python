salario = float(input("Qual é o salário do funcionário? R$"))

if salario <= 1250:
    aumento = salario * 0.15
    novoSalario = salario + aumento
else:
    aumento = salario * 0.1
    novoSalario = salario + aumento

print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora".format(salario, novoSalario))