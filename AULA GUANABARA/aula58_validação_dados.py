sexo = str(input('iNFORME SEU SEXO: [M/F] ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
