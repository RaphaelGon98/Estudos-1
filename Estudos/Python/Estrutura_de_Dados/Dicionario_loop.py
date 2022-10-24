from optparse import Values


aluno = {'nome': 'ana',
         'idade': 16,
         'nota_final': 'A',
         'Aprovação': True,
         'materias': ['python', 'sql']}

for keys, Values in aluno.items():
    print(keys, Values)

print(aluno.get('materias'))
