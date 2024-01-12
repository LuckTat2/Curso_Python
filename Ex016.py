dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
total_pag = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total_pag))