valor = float(input('Quanto custa o produto? R$'))
desconto = valor * 0.05     # 5/100 = 0.05
novo_valor = valor - desconto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor,novo_valor))