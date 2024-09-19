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
print(calculo_cpf)
