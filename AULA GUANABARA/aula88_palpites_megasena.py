import random, time
num = int(input('quantos jogos quer fazer? '))
for i in range(0, num):
    print(f'jogos {i+1}:', end=" ")
    bet = random.sample(range(1, 61), 6)
    print(sorted(bet))
    time.sleep(2)