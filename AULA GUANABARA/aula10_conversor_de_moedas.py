real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/4.92
euro = real/5.37
print('Com {:.2f} você pode comprar: \nUS${:.2f} \nEUR${:.2f}'.format(real,dolar,euro))
