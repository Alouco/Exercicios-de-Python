#def titulo(txt):
#    print('-' * 30)
#    print(txt)
#    print('-' * 30)
#
##programa principal
#titulo('ALUIZIO')
#titulo('aluu')
#titulo('oi')

#def soma(a, b, c):
#    print(f'A = {a} e B = {b} e C = {c}')
#    s = a + b + c
#    print(f'A soma A + B + C = {s}')
#
#
##programa principal
#soma(2,5,6)
#soma(2,8,8)
#soma(2,3,1)


#def contador(*num):
#    qtd = len(num)
#    print(f'Recebi os valores {num} e são ao todo {qtd} numeros')
#    
#    
#contador(2,1)
#contador(2,1,7)
#contador(2,1,7,9,2,3)

#def dobra(lst):
#    pos = 0
#    while pos < len(lst):
#        lst[pos] *= 2
#        pos += 1
#        
#valores = [6 ,3 ,9 ,1 , 0, 2]
#dobra(valores)
#print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

#programa principal
soma(2,5,6)
soma(2,8,8)
soma(2,3,1)