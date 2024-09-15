"""
Laço For em Python
Iterando string com for
Função range (start=0, stop, step=1)
"""

#Contagem Progressiva
for c in range(1, 6, 1):
    if c % 3 == 0:
        print(c)

print("########################################")
print("########################################")

#Contagem Regressiva
for n in range(10, 0, -1):
    print(n)

print("########################################")
print("########################################")

texto = "Python"
nova_string = ""

for letra in texto:
    if letra == "t":
        nova_string += letra.upper()
    elif letra == "h":
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

