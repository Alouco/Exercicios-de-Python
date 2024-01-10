def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade}. NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}. VOTO OPCIONAL!'
    else:
        return f'Com {idade}. VOTO OBRIGATORIO!'
    
nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))
        