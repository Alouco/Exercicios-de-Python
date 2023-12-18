aluno = dict()
aluno['nome'] = str(input('Aluno: '))
aluno['media'] = float(input(f'A Media de {aluno["nome"]}: '))

if aluno["media"]>= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
    
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
    
