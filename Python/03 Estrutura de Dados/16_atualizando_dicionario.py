

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

aluno.update({'nome': 'Jose', 'nota_final': 'B', 'endereço': 'Rua A'})

print(aluno)
print(aluno.get('cor', 'Não existe'))

del aluno['idade']
print(aluno)