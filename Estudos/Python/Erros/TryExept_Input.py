# Erros
# Exelentes para testes
# mensagens customizadas quando encontra um erro


try:

    valor = int(input('Digite o valor do seu produto: '))

    print(type(valor))
except ValueError:
    print('favor digitar um valor em numeros')
else:
    print(valor)
finally:
    print('codigo ok')
