#sets (listas)
# similar a listas
# evita itens duplicados
# não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

# "|" serve para tirar itens repetidos quando se une listas se chama UNION
print(num1 | num2)

print(num1 - num2)  # Diference, Retira numeros iguais

print(num1 ^ num2)  # Symmetrix Difference

print(num1 & num2)  # And

print(len(num1))
