def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('POR FAVOR DIGITE UM NUMERO INTEIRO VALIDO')
            continue
        except(KeyboardInterrupt):
            print('USUARIO PREFERIU NAO DIGITAR ESSE NUMERO')
            return 0
        else:
            return n 
        
        
        
def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc = LeiaInt('Sua Opcao: ')
    return opc