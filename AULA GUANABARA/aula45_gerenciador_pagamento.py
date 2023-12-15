preco = float(input('Preco das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartao
[4] 3x ou mais no cartão''')

opcao = int(input('Qual a opção? '))

if opcao == 1:
    total = preco - (preco - 10/100)
elif opcao == 2:
    total = preco - (preco - 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparc,parcela))
else:
    total = preco
    print('Opção invalida!')

print('Sua compra de R$ {:.2f} vai passar a custar R${:.2f}'.format(preco,total))