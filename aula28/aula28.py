nome = input("Qual o seu nome? ")
sobrenome = input("Qual o seu sobrenome? ")

if nome:
    print(f"Seu nome é {nome}")
else:
    print("Nome está vazio.")

#checa a primeira expressão, se ela for falsa passa para próxima, e sempre vai parar na primeira expressão verdadeira encontrada.
print(f"Seu sobrenome é {sobrenome}" or "Sobrenome está vazio")
