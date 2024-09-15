"""
Jogo de descobrir a palavra
"""

palavra_secreta = "perfume"
digitadas = []
tentativas = 3
while True:

    letra = input("Digite uma letra: ")

    #checa se foi digitado apenas uma letra
    if len(letra) > 1:
        print("Digite apenas uma letra!!!")
        continue #pula para proxima iteração do laço, sem sair do laço e nem executar nada abaixo.

    #Inserindo a letra que o usuário digitou na lista
    digitadas.append(letra)

    #Checando se a letra digitada está contida na string "secreto".
    if letra in palavra_secreta:
        print(f'Parabéns, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Não foi dessa vez, a letra "{letra}" não existe na palavra secreta.')
        digitadas.pop() #Removendo a letra errada da lista
        tentativas -= 1 #decrementa o número de tentativas
        print(f"Numero de tentativas {tentativas} restantes.")

    #Verifica se o jogador ainda tem tentativas, caso não, para o jogo.
    if tentativas == 0:
        print("Você perdeu!")
        break

    palavra_secreta_temporaria = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            palavra_secreta_temporaria += letra_secreta
        else:
            palavra_secreta_temporaria += "*"

    if palavra_secreta_temporaria == palavra_secreta:
        print(f"Parabéns!! Você ganhou! A palvra secretá é {palavra_secreta}")
        break
    else:
        print(f"A palavra secreta está assim: {palavra_secreta_temporaria}")
