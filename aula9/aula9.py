#Estrutura condicional e Operadores relacionais

"""
== igualdade
> maior
< menor
>= maior ou igual
<= menor ou igual
!= diferente

"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

maior_idade = 60 #passou da idade
menor_idade = 20 #muito jovem

if idade >= menor_idade and idade <= maior_idade:
    print(f"{nome.title()} pode pegar empréstimo.")
else:
    print(f"{nome} não pode pegar empréstimo.")
