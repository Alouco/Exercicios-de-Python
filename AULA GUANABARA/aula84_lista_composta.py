from time import sleep

pessoas = []
dado_temp = []
maior_peso_nome = []
menor_peso_nome = []
menor_peso = maior_peso = 0
while True:
    dado_temp.append(str(input('Nome:')))
    dado_temp.append(int(input('Peso:')))

    if len(pessoas) == 0:
        maior_peso = menor_peso = dado_temp[1]
        menor_peso_nome.append(dado_temp[0])
        maior_peso_nome.append(dado_temp[0])
    else:
        if dado_temp[1] == maior_peso:
            maior_peso_nome.append(dado_temp[0])
        if dado_temp[1] == menor_peso:
            menor_peso_nome.append(dado_temp[0])
        if dado_temp[1] > maior_peso:
            maior_peso = dado_temp[1]
            maior_peso_nome.clear()
            maior_peso_nome.append(dado_temp[0])
        if dado_temp[1] < menor_peso:
            menor_peso = dado_temp[1]
            menor_peso_nome.clear()
            menor_peso_nome.append(dado_temp[0])

    pessoas.append(dado_temp[:])
    dado_temp.clear()

    while True:
        continuar = str(input('Quer continuar?[S/N]:')).strip()
        if continuar in 'SsNn':
            break

    if continuar in 'Nn':
        print('Analisando dados..')
        sleep(2)
        break

print(f'\nAo todo você cadastrou {len(pessoas)} pessoas.'
      f'\nO maior peso foi de {maior_peso}Kg. peso de {maior_peso_nome}'
      f'\nO menor peso foi de {menor_peso}Kg. Peso de {menor_peso_nome}.')
