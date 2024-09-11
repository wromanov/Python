"""
Escreva um programa que paça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

numero = input("Informe o número: ")

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f"Numero {numero} é Par.")
    else:
        print(f"Numero {numero} é Impar.")
except:
    print("O número não é inteiro.")