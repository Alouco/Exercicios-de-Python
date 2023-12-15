velocidade  = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é o de 80Km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')