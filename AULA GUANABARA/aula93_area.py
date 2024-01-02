def area (larg, comp):
    a = larg * comp
    print(f'A area desse terreno é de {larg} X {comp} é de {a}m²')
    
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)