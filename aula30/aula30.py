cpf = input('Digite o CPF: ')

#removendo "." e "-"
cpf = cpf.replace(".","").replace("-","")

#convertendo o cpf em uma lista
cpf = cpf.split("")

print(len(cpf))


# lista_int = []

#cria uma nova lista com inteiros
# for i in lista:
#     lista_int.append(int(i))

# contagem = 10
# soma_cpf = 0
#
# for c in lista_int:
#     soma_cpf += c * contagem
#     contagem -= 1
#     print(soma_cpf)
