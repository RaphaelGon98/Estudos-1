#for numero in range(1,20,2): #numero
#    print (numero)

#palavra= 'espetacular'
#for letra in palavra:
#   print(f'{letra} esta dentro da palavra {palavra}') #for em string

compra_confirmada= True
dados_compra='compra no valor de R$ 12,.50 e entrega confirmada'
for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('detalhes enviado para seu email')
        break

else:
        print('falha na compra')

