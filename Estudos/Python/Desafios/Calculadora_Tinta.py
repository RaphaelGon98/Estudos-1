rendimento = int(input('qual o rendimento da lata em m²? '))
altura = int(input('qual a altura da parede? '))
largura = int(input('qual a largura da parede? '))

total = altura*largura
resultado = total/rendimento

print(   f'Voce vai precisar de {str(resultado)} latas de tinta para pintar sua parede ')
