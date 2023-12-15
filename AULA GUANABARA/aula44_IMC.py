peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você esta ABAIXO DO PESO NORMAL!')
elif 18.5 <= imc < 25:
    print('PARABENS! voce esta na faixa de peso normal!')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO!')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE!')
elif imc >= 40:
    print('Voce esta em OBESIDADE MORBIDA, cuidado!') 