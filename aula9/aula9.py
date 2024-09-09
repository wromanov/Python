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

if idade >= maior_idade and idade <= menor_idade:
    print(f"{nome} pode pegar empréstimo")
