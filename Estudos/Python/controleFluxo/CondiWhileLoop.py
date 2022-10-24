valor =int (input('digite o valor do seu produto '))
while valor >20:
    valor = (valor*0.10) + valor
    print(f'valor final do seu produto é R$ {valor}')
    break
