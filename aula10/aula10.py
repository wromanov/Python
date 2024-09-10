"""
Operadores Lógicos
and, or, not
in e not in
"""

a = bool("") #valor booleano igual a "False", pois a string está vazia.
b = bool(0) #valor booleano igual a "False", pois o valor é 0.
c = ""
d = 0
nome = "Walace"
print(a)
print(b)

#nega o valor, tranforma o valor no oposto, se for false, se torna true e vice versa.
if not a:
    print("Por favor, preencha o valor de A.")
else:
    print("Está preenchido.")

if "a" in nome:
    print("Letra existe.")
else:
    print("Letra não existe.")

if "a" not in nome:
    print("Letra não está contida.")
else:
    print("Letra está contida.")