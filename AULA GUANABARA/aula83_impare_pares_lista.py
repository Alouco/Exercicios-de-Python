num = list()
par = list()
impar = list()

while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
    
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
        
print(f'A lista completa é {num}')
print(f'os numeros pares sao  {par}')
print(f'os numeros impares sao {impar}')


numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    if input('Quer continuar? [S/N]').strip().upper() == 'N':
        break
    
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        
print(f'A lista completa é {numeros}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')