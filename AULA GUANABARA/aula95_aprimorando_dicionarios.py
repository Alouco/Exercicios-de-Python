#time = []
#gols = []
#jogador = dict()
#qual = 0
#
#while True:
#    jogador['nome'] = str(input('Nome do jogador: '))
#    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#    for c in range(0, partidas):
#        gol = int(input(f'Quantos gols na partida {c + 1}? '))
#        gols.append(gol)
#    jogador['gols'] = gols[:]
#    jogador['total'] = sum(gols)
#    gols.clear()
#    time.append(jogador.copy())
#
#    while True:
#        continuar = str(input('Quer continuar? [S/N] ').strip().upper())
#        if continuar in 'S,N':
#            break
#        print('ERRO! Responda apenas S ou N.')
#    if continuar in 'N':
#        break
#print('-=-' * 30)
#print('cod nome             gols           total')
#print('-' * 40)
#
#for b, d in enumerate(time):
#    print(f'{b}  {d["nome"]}    {d["gols"]}      {d["total"]}')
#print('-' * 40)
#while qual != 999:
#    qual = int(input('Mostrar dados de qual jogador? (999 para parar) '))
#    print(f'--- LEVANTAMENTO DO JOGADOR {time[qual]["nome"]}:')
#    for pos, g in enumerate(time[qual]['gols']):
#        print(f'No jogo {pos} fez {g} gols.')

time = []

while True:
    jogador = {'nome': input('Nome do jogador: '), 'gols': []}
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    for c in range(partidas):
        gol = int(input(f'Quantos gols na partida {c + 1}? '))
        jogador['gols'].append(gol)
    
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

print('-=-' * 15)
print('cod nome             gols           total')
print('-' * 40)

for b, jogador in enumerate(time):
    print(f'{b}  {jogador["nome"]}    {jogador["gols"]}      {jogador["total"]}')

print('-' * 40)

while True:
    qual = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    
    if qual == 999:
        break
    
    print(f'--- LEVANTAMENTO DO JOGADOR {time[qual]["nome"]}:')
    for pos, g in enumerate(time[qual]['gols']):
        print(f'No jogo {pos} fez {g} gols.')
