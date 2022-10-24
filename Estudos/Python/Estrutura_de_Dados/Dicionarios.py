# Dicionarios
# utiliza index no formato de keys e values
# aceota stromg, interger, float, boolean...

aluno = {'nome': 'ana', 'idade': 16, 'nota_final': 'A', 'Aprovação': True}

aluno.update({'endereço': 'rua a'})

print(aluno.get('endereço', 'Não existe'))
