"""
Split = A função split separa uma string e transforma as frases em itens de uma lista.
Join - Juntar os itens de uma lista
Enumerate - Enumerar elementos de uma lista.
count - conta a quantidade de vezes que uma string apareceu em uma lista ou em uma string.
strip - Remove os espaços em branco do inicio e fim da string
capitalize - Faz com que o primeiro caracter da string fique maiusculo.
"""

string = "O Brasil é o país do futebol, o Brasil é penta."

lista1 = string.split(" ")  # utilizamos o spaço como delimitador para a separação.
lista2 = string.split(",")  # utilizamos a vírgula como delimitador para a separação.

print(lista1)
print(lista2)

for valor in lista1:
    print(f"A palavra '{valor}' apareceu {lista1.count(valor)}x na frase.")

contagem = 0

#Verifica qual palavra apareceu mais vezes
for valor in lista1:
    quantidade_vezes = lista1.count(valor)
    if quantidade_vezes > contagem:
        contagem = quantidade_vezes
        palavra = valor

print(f"A palavra que apareceu mais vezes é {palavra} {contagem}x na frase.")

lista3 = ".".join(lista1)
print(lista3)

for indice, valor in enumerate(lista3):
    print(indice, valor)