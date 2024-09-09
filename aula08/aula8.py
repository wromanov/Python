#Criar variáveis para nome, idade, altura e peso de uma pessoa.
#Criar variável para o ano atual.
#Obter ano de nascimento da pessoa (baseado na idade e no ano atual)
#Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
#Exibir um texto com todos os valores na tela usando F-Strings
from datetime import date

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))
imc = peso / (altura * altura)
ano_atual = date.today().year
ano_nascimento = ano_atual - idade

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.")
print(f"{nome} nasceu em {ano_nascimento}.")


