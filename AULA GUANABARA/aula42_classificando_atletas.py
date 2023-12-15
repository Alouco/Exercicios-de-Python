from datetime import date
atual = date.today().year
nascimento = int(input('Data de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('O atleta é MIRIM.')
elif idade <= 14:
    print('O atleta é infantil.')
elif idade <= 19:
    print('O atleta é Junior.')
elif idade <= 25:
    print('O atleta é Sênior.')
else:
    print('O atleta é Master.')