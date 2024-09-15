"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, min, max, rang
"""
#        0      1     2  3  4
l1 = [1, "Walace", 3, 4, 5]
#     -  5     4      3  2  1

l2 = [6, 7, 8, 9, 10]

#juntando listas
l3 = l1 + l2

print(l3)

#acessando a lista
print(l1[1:4:2])

#fatiando item da lista
print(l1[1][0:3])

#lista de trás para frente
print(l1[::-1])

#ultimo ítem da lista
print(l1[-1])

#primeiro item da lista
print(l1[0])

#alterando valor de um item diretamente
l1[1] = "Eliane"
print(l1[1])
