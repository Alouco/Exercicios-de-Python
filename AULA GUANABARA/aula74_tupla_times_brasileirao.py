times = (
    'Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Fluminense', 'São Paulo',
    'Grêmio', 'Internacional', 'Athletico Paranaense', 'Cruzeiro', 'Botafogo',
    'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Ceará',
    'Santos', 'Chapecoense', 'Avaí', 'CSA'
)
print('-=' * 15)
print(f'Lista de time do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {times[-4:]}')
print('-=' * 15)
print(f'times em ordem alfabetica {sorted(times)}')
print('-=' * 15)
print(f'O São Paulo esta na {times.index("São Paulo")+1}ª posição')
