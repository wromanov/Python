#Intrudução formatação de string

"""Iniciar com letra, pode conter números, separar com _, letras minúsculas"""
import math

nome = "Walace"
idade = 34
altura = 1.74
e_maior = idade > 18
peso = 97
imc = peso / (math.pow(altura, 2))
#imc = peso / (altura ** 2)

#método 1
print(f"{nome} tem {idade} anos de idade, seu IMC é {imc:.2f}.")

#método 2
print("{} tem {} anos de idade, seu IMC é {:.2f}.".format(nome, idade, imc))

#parâmetros nomeados
print("{n} tem {i} anos de idade, seu IMC é {im:.2f}.".format(n=nome, i=idade, im=imc))

#dando ordem aos parâmetros
print("{0} tem {1} anos de idade, seu IMC é {2:.2f}.".format(nome, idade, imc))

