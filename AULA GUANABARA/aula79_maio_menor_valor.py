listanum = []

for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    
print(f'Voce digitou os valores {listanum}')
print(f'O menor valor foi {min(listanum)} nas posições ',end='')
for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'{i}...',end='')

print(f'\nO maior valor foi {max(listanum)} nas posições ',end='')
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'{i}...',end='')
    