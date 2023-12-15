frase = str(input('Digite uma frase: ')).strip().upper()
palvaras = frase.split()
junto = ''.join(palvaras)

inverso = ''
for letra in range(len(junto) - 1, -1,-1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palíndromo!')