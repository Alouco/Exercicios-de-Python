lista = [[], []]

for c in range(1, 8):
    valor = (int(input(f'Digite o {c}° valor: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    if valor % 2 == 1:
        lista[1].append(valor)

lista[1].sort()
lista[0].sort()
print('-=-' * 30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')