"""
Formatação de Valores
:s - Textos (Strings)
d: - Inteiros
:f - Floats
:.(numero)f - Quantidade de casas decimais (float):.2f
:(Caractere) (> ou < ou ^) (quantidade (tipo -s, d ou f)
> - Esquerda
< - Direita
^- Centro
"""

nome = "Walace"
num1 = 10
num2 = 3
divisao = num1 / num2

print(f"{nome:@>10}") #insere caracteres a esquerda

print(f"{nome:#<10}") #insere caracteres a direita

print(f"{divisao:.2f}") #Formata com 2 casas decimais

print(f"{divisao:0^10.2f}") #Formata centralizando zeros a esquerda e direita

print(f"{nome.upper()}") #Tudo minusculo
print(f"{nome.lower()}") #Tudo maiúsculo
print(f"{nome.title()}") #Tudo como titulo
