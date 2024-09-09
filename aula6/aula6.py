#Variáveis

"""Iniciar com letra, pode conter números, separar com _, letras minúsculas"""
import math

nome = "Walace"
idade = 34
altura = 1.74
e_maior = idade > 18
peso = 97
imc = peso / (math.pow(altura, 2))

print(f"{nome} tem {idade} anos de idade, seu IMC é {imc:.2f}.")
