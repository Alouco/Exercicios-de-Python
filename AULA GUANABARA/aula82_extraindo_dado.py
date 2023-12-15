valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'Voce digitou {len(valores)}.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O 5 faz parte da lista.')
else:
    print('O 5 nao esta na lista')
        