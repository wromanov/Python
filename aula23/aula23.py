"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, min, max, rang
"""
#        0      1     2  3  4
l1 = [1, "Walace", 3, 4, 5]
#     -  5     4      3  2  1

l2 = [6, 7, 8, 9, 10]

#Criando uma lista de forma mais fácil com a função list
l3 = list(range(1, 100))

#extendendo uma lista
l1.extend(l2)
print(l1)

#adicionado um elemento no final da lista
l1.append(11)
print(l1)

#inserindo um elemento na lista em um índice especifico
l1.insert(0, 0)
print(l1)

#removendo o último item da lista
l1.pop()
print(l1)

#removendo um índice específico da lista
l1.pop(0)
print(l1)

#removendo uma fatia de índices
del (l1[0:4])
print(l1)

#obtendo o maior e o menor valor da lista
print(max(l1))
print(min(l1))