temperatura = int(input('qual a temperatura da carne?'))

if temperatura < 48:
    print('cozinhar mais um pouco')
elif temperatura < 53:
    print('ao ponto para o mal')
elif temperatura < 59:
    print('ao ponto')
elif temperatura < 64:
    print('ao ponto para o bem')
elif temperatura > 71:
    print('bem passada')
