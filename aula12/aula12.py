"""
Funções built-in python
isdigit
isdecimal
isnumeric
somente retorna true se o numero for positivo e inteiro.

"""

numero01 = input("Informe o primeiro número: ")
numero02 = input("Informe o segundo número: ")

# método 1
try:
    numero01 = float(numero01)
    numero02 = float(numero02)
    print(numero01 + numero02)
except:
    print("ERROR")

# método 2
# if numero01.isnumeric() and numero02.isnumeric():
#     numero01 = float(numero01)
#     numero02 = float(numero02)
#     print(numero01 + numero02)
# else:
#     print("ERROR")
