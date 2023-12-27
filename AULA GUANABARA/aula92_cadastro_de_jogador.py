jogador = dict()
partida = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
for g in range(1, tot):
    partida.append(int(input(f'  Quantos Gols na partida {g}? ')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print('-=' * 30)
print(jogador)
print('-=' * 30)

for j, p in jogador.items():
    print(f'o campo {j} tem o valor {p}')
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i,v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')    