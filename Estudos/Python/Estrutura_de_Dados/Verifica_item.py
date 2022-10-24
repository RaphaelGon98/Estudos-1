cor_cliente = input('digite a cor desejada: ')

cores = ['amarelo', 'verde', 'azul', 'vermelho', ]

if cor_cliente.lower() in cores:
    print('em estoque')
else:
    print('Não tem em estoque')
