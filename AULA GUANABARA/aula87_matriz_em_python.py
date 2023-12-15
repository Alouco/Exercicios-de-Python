matriz = [[], [], []]

spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if c == 2:  # Verifica se é a última coluna
            scol += matriz[l][c]
        if l == 1:  # Verifica se está na segunda linha
            if c == 0 or matriz[l][c] > mai:
                mai = matriz[l][c]

    print()

print('-=' * 30)

print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {mai}')
