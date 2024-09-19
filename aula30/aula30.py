#Validador de CPF


cpf = input('Digite o CPF: ')

# removendo "." e "-"
cpf = cpf.replace(".", "").replace("-", "")

#Cria uma nova lista para inserir os números do CPF
lista_cpf = []

# percorre a string CPF
for digito in cpf:
    # print(digito)
    lista_cpf.append(int(digito))  # insere os dígitos da string cpf na lista_cpf

contagem = 10
soma_cpf = 0

for c in range(0, 9):
    soma_cpf += lista_cpf[c] * contagem  # multiplica o digito do cpf com o contador e adiciona ao acumulador
    contagem -= 1  # Decrementa a contagem
    #print(soma_cpf)

calculo_cpf = 11 - (soma_cpf % 11)

valida_digita_1 = 0

#valida o penúltimo digito do CPF
if calculo_cpf > 9:
    valida_digito_1 = 0
else:
    valida_digito_1 = calculo_cpf

print(f"Calculo do CPF {calculo_cpf} Valor do Penúltimo Dígito {valida_digito_1}")

#valida o último digito do CPF
soma_cpf_2 = 0
contagem_2 = 11

for k in range(0, 10):
    soma_cpf_2 += lista_cpf[k] * contagem_2
    print(soma_cpf_2, lista_cpf[k], contagem_2)
    contagem_2 -= 1  # Decrementa a contagem
    if contagem_2 == 2:
        soma_cpf_2 += valida_digito_1 * contagem_2  # multiplica o digito do cpf com o contador e adiciona ao acumulador
        contagem_2 -= 1  # Decrementa a contagem
        print(soma_cpf_2)
        break

calculo_cpf_2 = 11 - (soma_cpf_2 % 11)

valida_digito_2 = 0

#valida o último digito do CPF
if calculo_cpf_2 > 9:
    valida_digito_2 = 0
else:
    valida_digito_2 = calculo_cpf_2

print(f"Calculo do CPF {calculo_cpf_2} Valor do Penúltimo Dígito {valida_digito_2}")