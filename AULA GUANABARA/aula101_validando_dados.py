def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[0;31m')
        if ok:
            break
    return valor

#Programa principal

n = LeiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')