
frase = "O rato roeu a roupa do rei de roma."
tamanho_frase = len(frase)
contador = 0
nova_string = ""
escolha = input("Qual letra deseja colocar maiúscula? ")

while contador < tamanho_frase:
    #print(frase[contador], contador)
    letra = frase[contador]
    if letra == escolha:
        nova_string += escolha.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)

