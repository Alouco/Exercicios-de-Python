from random import randint
from time import sleep
computador = randint(0,5) #faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) #o jogador tenta adivinhar
print('PROCESSANDO...')
if jogador == computador:
    print('PARABENS! Você conseguiu vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}'.format(computador,jogador))