numeros = list()

while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('valor duplicado!Não vou adicionar... ')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

numeros.sort()
print(f'Voce digitou os valores {numeros}')