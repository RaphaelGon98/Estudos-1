# List Comprehension
# mais simples para escrever
# ultilizado quando voce precisa criar uma nova lista a partir de uma existente
#[expressao for iten in itens]


# frutas2 = []
# for iten in frutas1:
#     if 'n' in iten:
#         frutas2.append(iten)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = [iten for iten in frutas1 if 'n' in iten]

# print(frutas2)

# 22222222222222222222222222222222222222222222222222222222222222222222222222
# valores = []

# for x in range(6):
#     valores.append(x*10)

# print(valores)

valores = [x * 10 for x in range(6)]
print(valores)
