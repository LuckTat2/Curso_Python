salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario * 0.15    # 15/100 = 0.15
novo_salario = salario + aumento
print('Um funcionário que ganhava R${:.2f}, com reajuste de 15%, passa a receber R${:.2f}'.format(salario,novo_salario))
