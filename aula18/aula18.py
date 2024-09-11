"""
Acessar caracter da string pelo índice
Fatiamento de String [Inicio:Fim:Passo]

"""
# índice positivo    [123456789]
texto              = "Python_s2"
# índice negativo   -[987654321]

nova_string = texto[1]
nova_string2 = texto[0:8]
nova_string3 = texto[0:9:2] #pula de dois em dois caracter


print(nova_string)
print(nova_string2)
print(nova_string3)