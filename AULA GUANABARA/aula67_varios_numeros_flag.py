#num = soma = 0
#while num != 999:
#    num = int(input('Digite um numero [DIGITE 999 PARA PARAR]:'))
#    soma += num
#soma -= 999
#print(f'O valor final é {soma}')

soma = cont = 0
while True:
    num = int(input('Digite um numero [DIGITE 999 PARA PARAR]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores foi {soma} e a contagem foi {cont}')